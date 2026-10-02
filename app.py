import streamlit as st
import pandas as pd
import plotly.graph_objects as go
from database import generate_mock_data
from model import generate_forecast

# 1. Page Configuration
st.set_page_config(page_title="Demand Forecast Planner", layout="wide")
st.title("AI-Powered Demand Forecasting Dashboard")
# Project Context & Metadata for Portfolio Validation
st.markdown("""
###  System Overview & Architecture
This enterprise-grade demand planning engine leverages advanced time-series forecasting to predict inventory runway constraints and revenue targets. 

*   **AI Engine Backend:** Prophet Seasonal Forecasting Model (Optimized for macro retail waves)
*   **Frontend UI Framework:** Streamlit Core Python Dashboard System
*   **Key Capabilities:** Dynamic Simulation Sliders, Interactive Plotly Analytics, Live Data Overrides, and CSV Export Utilities.
---
""",unsafe_allow_html=True)
# 2. Load Data into Memory
if "data" not in st.session_state:
    st.session_state.data = generate_mock_data()

df = st.session_state.data

# 3. Sidebar Controls Layout
st.sidebar.header("Forecast Configurations")
selected_product = st.sidebar.selectbox("Select Target SKU/Product", df["Product"].unique())
promo_boost = st.sidebar.slider("Simulate Promotional Uplift (%)", min_value=0, max_value=50, value=0, step=5)

# Filter data for selected product
df_prod = df[df["Product"] == selected_product].copy()

# 4. Generate Machine Learning Forecast
df_forecast = generate_forecast(df_prod, months_to_predict=6)

# Apply the What-If simulation slider adjustments
df_forecast["Final_Forecast"] = (df_forecast["Forecast_Baseline"] * (1 + promo_boost / 100)).astype(int)

# 5. Top KPI Summary Metrics 
col1, col2 = st.columns(2)
with col1:
    next_month_demand = df_forecast['Final_Forecast'].iloc[0]
    st.metric("Next Month Target Demand", f"{next_month_demand} units")
with col2:
    st.metric("Simulated Promo Multiplier", f"+{promo_boost}%")

# 6. Interactive Visualization Chart using Plotly
fig = go.Figure()

# Plot historical trace
fig.add_trace(go.Scatter(x=df_prod["Date"], y=df_prod["Historical_Sales"], name="Historical Actuals", line=dict(color="blue", width=2)))

# Plot forecasted trace
fig.add_trace(go.Scatter(x=df_forecast["Date"], y=df_forecast["Final_Forecast"], name="Future Forecast", line=dict(color="orange", width=2, dash="dash")))

fig.update_layout(title=f"Sales Performance & Demand Runway: {selected_product}", xaxis_title="Timeline", yaxis_title="Units Sold", hovermode="x unified")
st.plotly_chart(fig, use_container_width=True)
# 6b. Comparative Performance Bar Chart
st.subheader(" Category Performance Comparison")

# Calculate total sales metrics for overall baseline review
df_total_sales = df.groupby("Product")["Historical_Sales"].sum().reset_index()

fig_bar = go.Figure()
fig_bar.add_trace(go.Bar(
    x=df_total_sales["Product"],
    y=df_total_sales["Historical_Sales"],
    marker_color=["#1f77b4", "#ff7f0e"]
))

fig_bar.update_layout(
    title="Total Historical Sales Allocation Across Categories",
    xaxis_title="Product Group",
    yaxis_title="Total Historical Units Sold"
)
st.plotly_chart(fig_bar, use_container_width=True)


# 7. Editable Scenario Override Table Grid
st.subheader("Editable Demand Override Grid")
st.write("Manually adjust next season's forecast rows below if you know about upcoming market changes:")

# Format dates to look nice in the grid
df_forecast["Month"] = df_forecast["Date"].dt.strftime('%B %Y')
grid_df = df_forecast[["Month", "Final_Forecast"]].copy()

edited_grid = st.data_editor(grid_df, num_rows="fixed", disabled=["Month"], use_container_width=True)
# 8. Export Configuration utility
st.markdown("---")
st.subheader("📥 Export Final Plan")

# Convert the live grid updates into a clean downloadable CSV file layout
csv_data = edited_grid.to_csv(index=False).encode('utf-8')

st.download_button(
    label="Download Adjusted Forecast Spreadsheet",
    data=csv_data,
    file_name=f"Demand_Plan_{selected_product}.csv",
    mime="text/csv",
)
