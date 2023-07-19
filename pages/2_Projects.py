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



# Streamlit app



years = df['year'].unique()
years = [int(year) for year in years]
        
months = df['month'].unique()
month = [int(month) for month in months]

        # Year range selection using a slider
year_start, year_end = st.slider('Select year range', min_value=min(years), max_value=max(years), value=(min(years), max(years)))
month_start, month_end = st.slider('Select month range', min_value=min(month), max_value=max(month), value=(min(month), max(month)))


filtered_df = df[(df['year'] >= year_start) & (df['year'] <= year_end)]
filtered_df = filtered_df[(filtered_df['month'] >= month_start) & (filtered_df['month'] <= month_end)]


pivots = get_pivs(filtered_df)
selected_category = st.selectbox("Select a category", list(pivots.keys()))

if selected_category:
    st.subheader(f"Pivot Tables for {selected_category}")
    for pivot_heading, pivot_table in pivots[selected_category]:
        st.subheader(pivot_heading)
        st.dataframe(pivot_table)
