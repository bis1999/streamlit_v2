import streamlit as st
import pandas as pd 

st.title("Pivot tables ")
df = st.session_state["my_input"]
noaa_df = st.session_state["noaa"]




def pivotgen(df, val, agg_='mean', idx='month', cols='year'):
    return pd.pivot_table(df, values=val, index=idx, columns=cols, aggfunc=agg_, margins=True)

def get_pivs(df):
    Consumption = ["Cons_Elec", "Cons_ind", "Cons_Resi", "Cons_Comm", "Cons_pipefuel", "Cons_Vehfuel", "cons_plantfuel", "Cons_tot"]
    production = ["Prod_marketed", "ext_loss", "Prod_dry", "Prod_tot"]
    Underground_Storage = ["injections", "withdrawals", "Net_withdrawals", "Tot_working", "Base_gas", "tot_storage_cap"]
    Imports_Exports = ["imp_pipe", "imp_LNG", "imp_tot", "exp_pipe", "exp_LNG", "exp_tot"]
    prices = ["pr_elec_power", "pr_LNG_exp", "pr_exp", "pr_lng_import", "pr_imp", "pr_ind", "pr_citygate", "pr_pipeexp", "pr_resi", "pr_comml"]
    temp_spot_price = ["Price_HH", "Price_k1", "Price_k2", "Price_k3"]
    temp_cdd_hdd = ["hdd","hdd_dev","wcdd","wcdd_dev"]

    dt = {
        "production": production,
        "Consumption": Consumption,
        "Imports_Exports": Imports_Exports,
        "Underground_Storage": Underground_Storage,
        "prices": prices,
        "spot_price": temp_spot_price,
        "NOAA" : temp_cdd_hdd 
    }

    pivs = {}
    
    for i in list(dt.keys()):
        pivs[i] = []
        for j in dt[i]:
            if i == "spot_price":
                pivs[i].append((f"{i} - {j}", pivotgen(df, j, agg_='sum')))
            elif i == "NOAA":

                pivs[i].append((f"{i} - {j}", pivotgen(noaa_df, j, agg_='sum')))

            else:
                pivs[i].append((f"{i} - {j}", pivotgen(df, j)))

    return pivs

# Assuming you have the DataFrame 'your_dataframe' containing the data

# Get the pivot tables

st.sidebar.title("Pivot Tables Options")

# Default values for sliders and checkboxes
year_start, year_end = st.sidebar.slider('Select year range', min_value=2008, max_value=2023, value=(2017, 2023))
month_start, month_end = st.sidebar.slider('Select month range', min_value=1, max_value=12, value=(1, 12))

show_consumption_pivot = st.sidebar.checkbox("Show Consumption Pivot", value=True)
show_production_pivot = st.sidebar.checkbox("Show Production Pivot")
show_import_export_pivot = st.sidebar.checkbox("Show Imports/Exports Pivot")
show_underground_storage_pivot = st.sidebar.checkbox("Show Underground Storage Pivot")
show_prices_pivot = st.sidebar.checkbox("Show Prices Pivot")
show_spot_price_pivot = st.sidebar.checkbox("Show Spot Price Pivot")
#show_noaa_pivot = st.sidebar.checkbox("Show NOAA Pivot")

if (
    show_consumption_pivot
    or show_production_pivot
    or show_import_export_pivot
    or show_underground_storage_pivot
    or show_prices_pivot
    or show_spot_price_pivot
    or show_noaa_pivot
):
    years = df['year'].unique()
    years = [int(year) for year in years]

    months = df['month'].unique()
    month = [int(month) for month in months]

    filtered_df = df[(df['year'] >= year_start) & (df['year'] <= year_end)]
    filtered_df = filtered_df[(filtered_df['month'] >= month_start) & (filtered_df['month'] <= month_end)]

    pivots = get_pivs(filtered_df)

    if show_consumption_pivot:
        st.subheader("Pivot Tables for Consumption")
        for pivot_heading, pivot_table in pivots["Consumption"]:
            st.subheader(pivot_heading)
            st.dataframe(pivot_table)

    if show_production_pivot:
        st.subheader("Pivot Tables for Production")
        for pivot_heading, pivot_table in pivots["production"]:
            st.subheader(pivot_heading)
            st.dataframe(pivot_table)

    if show_import_export_pivot:
        st.subheader("Pivot Tables for Imports/Exports")
        for pivot_heading, pivot_table in pivots["Imports_Exports"]:
            st.subheader(pivot_heading)
            st.dataframe(pivot_table)

    if show_underground_storage_pivot:
        st.subheader("Pivot Tables for Underground Storage")
        for pivot_heading, pivot_table in pivots["Underground_Storage"]:
            st.subheader(pivot_heading)
            st.dataframe(pivot_table)

    if show_prices_pivot:
        st.subheader("Pivot Tables for Prices")
        for pivot_heading, pivot_table in pivots["prices"]:
            st.subheader(pivot_heading)
            st.dataframe(pivot_table)

    if show_spot_price_pivot:
        st.subheader("Pivot Tables for Spot Price")
        for pivot_heading, pivot_table in pivots["spot_price"]:
            st.subheader(pivot_heading)
            st.dataframe(pivot_table)







# Streamlit app
