import streamlit as st
import pandas as pd
import plotly.graph_objects as go

st.title("Time Series Plot")
your_dataframe = st.session_state["my_input"]

# Assuming you have the DataFrame 'your_dataframe' containing the data

# Get unique years and months
years = your_dataframe['year'].unique()
years = [int(year) for year in years]

months = your_dataframe['month'].unique()
months = [int(month) for month in months]

# Checkbox for selecting the categories
st.sidebar.title("Time Series Plot Options")




# Year range selection using a slider in the sidebar
year_start, year_end = st.sidebar.slider('Select year range', min_value=min(years), max_value=max(years), value=(min(years), max(years)))

# Month range selection using a slider in the sidebar
month_start, month_end = st.sidebar.slider('Select month range', min_value=min(months), max_value=max(months), value=(min(months), max(months)))


show_consumption = st.sidebar.checkbox("Show Consumption", value=True)
show_production = st.sidebar.checkbox("Show Production")
show_import_export = st.sidebar.checkbox("Show Imports/Exports")
show_underground_storage = st.sidebar.checkbox("Show Underground Storage")
show_prices = st.sidebar.checkbox("Show Prices")
show_spot_price = st.sidebar.checkbox("Show Spot Price")

# Filter the DataFrame based on the selected year and month ranges
filtered_df = your_dataframe[
    (your_dataframe['year'].between(year_start, year_end)) &
    (your_dataframe['month'].between(month_start, month_end))
]

if show_consumption:
    value_columns = ["Cons_Elec", "Cons_ind", "Cons_Resi", "Cons_Comm", "Cons_pipefuel", "Cons_Vehfuel", "cons_plantfuel", "Cons_tot"]
    fig = go.Figure()
    # Add lines based on the selected value columns
    for i, column in enumerate(value_columns):
        x = filtered_df['Period']
        y = filtered_df[column]
        fig.add_trace(go.Scatter(x=x, y=y, mode='lines', name=column))

    fig.update_layout(width=1000, height=700)
    fig.update_layout(title_text="Consumption Time Series Plot")
    # Display the time series plot for Consumption
    st.plotly_chart(fig)

if show_production:
    value_columns = ["Prod_marketed", "ext_loss", "Prod_dry", "Prod_tot"]
    fig = go.Figure()
    # Add lines based on the selected value columns
    for i, column in enumerate(value_columns):
        x = filtered_df['Period']
        y = filtered_df[column]
        fig.add_trace(go.Scatter(x=x, y=y, mode='lines', name=column))

    fig.update_layout(width=1000, height=700)
    fig.update_layout(title_text="Production Time Series Plot")
    # Display the time series plot for Production
    st.plotly_chart(fig)

if show_import_export:
    value_columns = ["imp_pipe", "imp_LNG", "imp_tot", "exp_pipe", "exp_LNG", "exp_tot"]
    fig = go.Figure()
    # Add lines based on the selected value columns
    for i, column in enumerate(value_columns):
        x = filtered_df['Period']
        y = filtered_df[column]
        fig.add_trace(go.Scatter(x=x, y=y, mode='lines', name=column))

    fig.update_layout(width=1000, height=700)
    fig.update_layout(title_text="Imports/Exports Time Series Plot")
    # Display the time series plot for Imports/Exports
    st.plotly_chart(fig)

if show_underground_storage:
    value_columns = ["injections", "withdrawals", "Net_withdrawals", "Tot_working", "Base_gas", "tot_storage_cap"]
    fig = go.Figure()
    # Add lines based on the selected value columns
    for i, column in enumerate(value_columns):
        x = filtered_df['Period']
        y = filtered_df[column]
        fig.add_trace(go.Scatter(x=x, y=y, mode='lines', name=column))

    fig.update_layout(width=1000, height=700)
    fig.update_layout(title_text="Underground Storage Time Series Plot")
    # Display the time series plot for Underground Storage
    st.plotly_chart(fig)

if show_prices:
    value_columns = ["pr_elec_power", "pr_LNG_exp", "pr_exp", "pr_lng_import", "pr_imp", "pr_ind", "pr_citygate", "pr_pipeexp", "pr_resi", "pr_comml"]
    fig = go.Figure()
    # Add lines based on the selected value columns
    for i, column in enumerate(value_columns):
        x = filtered_df['Period']
        y = filtered_df[column]
        fig.add_trace(go.Scatter(x=x, y=y, mode='lines', name=column))

    fig.update_layout(width=1000, height=700)
    fig.update_layout(title_text="Prices Time Series Plot")
    # Display the time series plot for Prices
    st.plotly_chart(fig)

if show_spot_price:
    value_columns = ["Price_HH", "Price_k1", "Price_k2", "Price_k3"]
    fig = go.Figure()
    # Add lines based on the selected value columns
    for i, column in enumerate(value_columns):
        x = filtered_df['Period']
        y = filtered_df[column]
        fig.add_trace(go.Scatter(x=x, y=y, mode='lines', name=column))

    fig.update_layout(width=1000, height=700)
    fig.update_layout(title_text="Spot Price Time Series Plot")
    # Display the time series plot for Spot Price
    st.plotly_chart(fig)
