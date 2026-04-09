import streamlit as st
import pandas as pd
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt

# Page config
st.set_page_config(
    page_title="Customer Segmentation & Churn Pattern Analytics in European Banking Dashboard",
    page_icon="💳",
    layout="wide"
)

# Load data
@st.cache_data
def load_data():
    return pd.read_csv('01_European_bank/Data/European_Bank.csv')

df = load_data()

# Derived fields
df['AgeGroup'] = pd.cut(df['Age'], bins=[0,30,45,60,100], labels=['<30','30-45','46-60','60+'])
df['CreditScoreBand'] = pd.cut(df['CreditScore'], bins=[300,600,750,850], labels=['Low','Medium','High'])
df['TenureGroup'] = pd.cut(df['Tenure'], bins=[0,3,7,10], labels=['New','Mid-term','Long-term'])
df['BalanceSegment'] = pd.cut(df['Balance'], bins=[-1,0,50000,250000], labels=['Zero','Low','High'])

# Sidebar filters
st.sidebar.header("Segment Filters")
geo_filter = st.sidebar.multiselect("Select Geography", sorted(df['Geography'].dropna().unique()))
age_filter = st.sidebar.multiselect("Select Age Group", [cat for cat in df['AgeGroup'].cat.categories if pd.notna(cat)])
tenure_filter = st.sidebar.multiselect("Select Tenure Group", [cat for cat in df['TenureGroup'].cat.categories if pd.notna(cat)])
balance_filter = st.sidebar.multiselect("Select Balance Segment", [cat for cat in df['BalanceSegment'].cat.categories if pd.notna(cat)])

# Apply filters
filtered_df = df.copy()
if geo_filter:
    filtered_df = filtered_df[filtered_df['Geography'].isin(geo_filter)]
if age_filter:
    filtered_df = filtered_df[filtered_df['AgeGroup'].isin(age_filter)]
if tenure_filter:
    filtered_df = filtered_df[filtered_df['TenureGroup'].isin(tenure_filter)]
if balance_filter:
    filtered_df = filtered_df[filtered_df['BalanceSegment'].isin(balance_filter)]

st.title("💳 Customer Segmentation & Churn Pattern Analytics in European Banking Dashboard")

# Tabs
tab1, tab2, tab3, tab4, tab5 = st.tabs(["KPIs", "Geography", "Age & Tenure", "High-Value Explorer", "Drill-down"])

# --- KPI Section ---
with tab1:
    st.subheader("Key Performance Indicators")

    # Calculate KPIs
    overall_churn = filtered_df['Exited'].mean() * 100
    segment_churn = (filtered_df.groupby("AgeGroup")["Exited"].mean() * 100).mean()
    high_value = filtered_df[filtered_df['BalanceSegment']=="High"]
    high_value_churn = high_value['Exited'].mean() * 100 if not high_value.empty else 0
    geo_churn = (filtered_df.groupby("Geography")["Exited"].mean() * 100)
    geo_risk = geo_churn.max() - geo_churn.min() if not geo_churn.empty else 0
    inactive_churn = filtered_df[filtered_df['IsActiveMember']==0]["Exited"].mean() * 100
    active_churn = filtered_df[filtered_df['IsActiveMember']==1]["Exited"].mean() * 100
    engagement_gap = inactive_churn - active_churn

    # First row
    col1, col2, col3 = st.columns(3)
    col1.metric("📊 Overall Churn Rate", f"{overall_churn:.2f}%")
    col2.metric("👥 Segment Churn (Age)", f"{segment_churn:.2f}%")
    col3.metric("💰 High-Value Churn", f"{high_value_churn:.2f}%")

    # Second row
    col4, col5, col6 = st.columns(3)
    col4.metric("🌍 Geographic Risk Index", f"{geo_risk:.2f}%")
    col5.metric("🔔 Engagement Drop", f"{engagement_gap:.2f}%")
    # col6 intentionally left empty for layout balance

    # --- Engagement Drop Visualization ---
    st.subheader("Engagement Drop Indicator")
    engagement_data = pd.DataFrame({
        "Status": ["Inactive", "Active"],
        "Churn %": [inactive_churn, active_churn]
    })

    fig_engagement = px.bar(
        engagement_data,
        x="Status",
        y="Churn %",
        color="Status",
        text="Churn %",
        labels={"Churn %":"Churn Percentage "},
        title="Churn Rate: Active vs Inactive Members",
        color_discrete_map={"Inactive":"red","Active":"green"}
    )
    fig_engagement.update_traces(texttemplate='%{text:.2f}%', textposition='outside')
    fig_engagement.update_yaxes(range=[0,30])
    st.plotly_chart(fig_engagement, use_container_width=True)

    # --- Segment Churn Visualization ---
    st.subheader("Churn Percentage by Age Segment")
    age_churn = filtered_df.groupby("AgeGroup")["Exited"].mean() * 100

    fig_age = px.bar(
        age_churn,
        x=age_churn.index,
        y=age_churn.values,
        text=age_churn.values.round(2),
        labels={"x":"Age Group","y":"Churn %"},
        title="Churn Percentage by Age Segment",
        color=age_churn.index,
        color_discrete_sequence=px.colors.qualitative.Pastel
    )
    fig_age.update_traces(textposition="outside")
    fig_age.update_yaxes(range=[0,60])
    st.plotly_chart(fig_age, use_container_width=True)

    # --- High-Value Churn Visualization ---
    st.subheader("High-Value Churn Ratio")
    if not high_value.empty:
        hv_data = pd.DataFrame({
            "Status": ["Premium Customers"],
            "Churn %": [high_value_churn]
        })

        fig_hv = px.bar(
            hv_data,
            x="Status",
            y="Churn %",
            text="Churn %",
            labels={"Churn %":"Churn Percentage"},
            title="Churn among Premium Customers",
            color="Status",
            color_discrete_map={"Premium Customers":"#FFB6C1"}  # light red/pink
        )
        fig_hv.update_traces(texttemplate='%{text:.2f}%', textposition='outside')
        fig_hv.update_yaxes(range=[0,45])
        st.plotly_chart(fig_hv, use_container_width=True)
    else:
        st.info("No high-value customers found for the current filter selection.")

# --- Geography ---
with tab2:
    st.subheader("Geography-wise Churn")
    geo_churn = filtered_df.groupby("Geography")["Exited"].mean() * 100

    # Define unique colors for the three countries
    country_colors = {
        "France": "#275CEF",
        "Germany": "#68CF68",
        "Spain": "#CD2A43"
    }

    # Bar chart with distinct colors per country
    fig = px.bar(
        geo_churn,
        x=geo_churn.index,
        y=geo_churn.values,
        color=geo_churn.index,
        text=geo_churn.values.round(2),   
        labels={"x":"Geography","y":"Churn %"},
        title="Geography-wise Churn",
        color_discrete_map=country_colors
    )

    # Add overall churn line for comparison
    fig.add_hline(
        y=overall_churn,
        line_dash="dash",
        line_color="black",
        annotation_text="Overall Churn",
        annotation_position="top left"
    )

    # Fix y-axis limit for clarity
    fig.update_yaxes(range=[0,50])

    st.plotly_chart(fig, use_container_width=True)

    # Display Geographic Risk Index value below chart
    st.write(f"🌍 **Geographic Risk Index:** {geo_risk:.2f}% (gap between highest and lowest churn regions)")


# --- Age & Tenure ---
with tab3:
    st.subheader("Age & Tenure Churn Comparison")

    age_tenure = filtered_df.groupby(["AgeGroup","TenureGroup"])["Exited"].mean().unstack() * 100

    fig = px.imshow(
        age_tenure,
        text_auto=True,
        color_continuous_scale="YlOrRd",
        labels=dict(x="Tenure Group", y="Age Group", color="Churn %"),
        title="Churn Percentage by Age & Tenure"
    )
    fig.update_layout(height=900, width=900, margin=dict(t=40,l=40,r=40,b=40))
    st.plotly_chart(fig, use_container_width=True)


# --- High-Value Explorer ---

with tab4:
    st.subheader("High-Value Customer Explorer")
    high_value = filtered_df[filtered_df['BalanceSegment']=="High"]

    # KPIs
    high_value_churn = high_value['Exited'].mean() * 100 if not high_value.empty else 0
    revenue_risk = high_value[high_value['Exited']==1]['Balance'].sum()

    col1, col2 = st.columns(2)
    col1.metric("💎 High-Value Churn Rate", f"{high_value_churn:.2f}%")
    col2.metric("💸 Revenue Risk (Lost Balance)", f"${revenue_risk:,.0f}")

    if not high_value.empty:
        # Bubble chart: Balance vs Salary
        fig_bubble = px.scatter(
            high_value,
            x="Balance",
            y="EstimatedSalary",
            size="NumOfProducts",          # bubble size shows products held
            color="Exited",                # churn status
            labels={"Balance":"Customer Balance","EstimatedSalary":"Estimated Salary","Exited":"Churned"},
            title="High-Value Customers: Balance vs Salary",
            color_discrete_map={0:"green",1:"red"}
        )
        fig_bubble.update_layout(height=800, width=1200, margin=dict(t=60,l=60,r=60,b=60))
        st.plotly_chart(fig_bubble, use_container_width=True)

        # Boxplot: Balance distribution by churn status
        fig_box = px.box(
            high_value,
            x="Exited",
            y="Balance",
            color="Exited",
            labels={"Exited":"Churned","Balance":"Customer Balance"},
            title="Balance Distribution by Churn Status",
            color_discrete_map={0:"green",1:"red"}
        )
        
        # Update x-axis tick labels
        fig_box.update_xaxes(
            tickvals=[0,1],
            ticktext=["Not Churned","Churned"]
        )
        
        # Update legend labels
        fig_box.for_each_trace(
            lambda t: t.update(name="Not Churned" if t.name=="0" else "Churned")
        )
        fig_box.update_layout(height=600, width=900, margin=dict(t=40,l=40,r=40,b=40))
        st.plotly_chart(fig_box, use_container_width=True)

# --- Drill-down ---
with tab5:
    st.subheader("Drill-down Segment Profiles")
    styled_table = (
        filtered_df.groupby("Exited")[['Age','CreditScore','Balance','EstimatedSalary','NumOfProducts']]
        .mean()
        .round(2)
        .style.background_gradient(cmap="Blues")
    )
    st.dataframe(styled_table, use_container_width=True)
