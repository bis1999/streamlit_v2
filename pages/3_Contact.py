import streamlit as st

import streamlit as st
import pandas as pd
import plotly.graph_objects as go

st.title("Time Series Plot")

your_dataframe = st.session_state["my_input"]

# Assuming you have the DataFrame 'your_dataframe' containing the data

years = your_dataframe['year'].unique()
years = [int(year) for year in years]

months = your_dataframe['month'].unique()
months = [int(month) for month in months]

# Year range selection using a slider
year_start, year_end = st.slider('Select year range', min_value=min(years), max_value=max(years), value=(min(years), max(years)))
month_start, month_end = st.slider('Select month range', min_value=min(months), max_value=max(months), value=(min(months), max(months)))

# Filter the DataFrame based on the selected year and month ranges
filtered_df = your_dataframe[
    (your_dataframe['year'].between(year_start, year_end)) &
    (your_dataframe['month'].between(month_start, month_end))
]

# Dropdown menu for selecting the category
categories = ["Consumption", "production", "Imports_Exports", "Underground_Storage", "prices", "spot_price","NOAA"]
selected_category = st.selectbox("Select a category", categories)

# List of value columns based on the selected category
value_columns = []
if selected_category == "Consumption":
    value_columns = ["Cons_Elec", "Cons_ind", "Cons_Resi", "Cons_Comm", "Cons_pipefuel", "Cons_Vehfuel", "cons_plantfuel", "Cons_tot"]
elif selected_category == "production":
    value_columns = ["Prod_marketed", "ext_loss", "Prod_dry", "Prod_tot"]
elif selected_category == "Imports_Exports":
    value_columns = ["imp_pipe", "imp_LNG", "imp_tot", "exp_pipe", "exp_LNG", "exp_tot"]
elif selected_category == "Underground_Storage":
    value_columns = ["injections", "withdrawals", "Net_withdrawals", "Tot_working", "Base_gas", "tot_storage_cap"]
elif selected_category == "prices":
    value_columns = ["pr_elec_power", "pr_LNG_exp", "pr_exp", "pr_lng_import", "pr_imp", "pr_ind", "pr_citygate", "pr_pipeexp", "pr_resi", "pr_comml"]
elif selected_category == "spot_price":
    value_columns = ["Price_HH", "Price_k1", "Price_k2", "Price_k3"]



fig = go.Figure()

# Add lines based on the selected value columns
for i, column in enumerate(value_columns):

    x = filtered_df['Period']
    y = filtered_df[column]
    fig.add_trace(go.Scatter(x=x, y=y, mode='lines', name=column))

fig.update_layout(width=1000, height=700)

# Display the time series plot
st.plotly_chart(fig)
