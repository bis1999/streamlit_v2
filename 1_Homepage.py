import streamlit as st
import pandas as pd
from EIAmonth import scaling_and_renaming
from datetime import date
import plotly.graph_objects as go
import glob
import os
from tqdm import tqdm 



st.set_page_config(
    page_title="Multipage App",
    page_icon="👋",
)

st.title("Main Page")
st.sidebar.success("Select a page above.")


## EIA MONTHLY
datasets = glob.glob('Data/*.csv')
dates = [i.split(".")[0].split("/")[1] for i in datasets]
data_ = max(dates)

st.write("Last Updated EIA Gas monthly: {} ".format(data_ ))
st.write("Data Source : https://www.eia.gov/dnav/ng/ng_sum_lsum_dcu_nus_m.htm")
if st.button("Update EIA Gas monthly"):
        # Call the function to update the dataset
        df = scaling_and_renaming()# # Reload the updated dataset
        today = date.today()
        st.write("Natural Gas Monthly Data Updated on {}".format(str(today)))

      
        
else:
    
    df = pd.read_csv("Data/{}.csv".format(data_))


### Done



### NOAA 
datasets = glob.glob('Data/*.csv')
dates = [i.split(".")[0].split("/")[1] for i in datasets]
data_ = max(dates)

st.write("Last Updated NOAA: {} ".format(data_ ))
if st.button("Update NOAA monthly"):
        # Call the function to update the dataset
        noaa= pd.read_csv("NOAA.csv")# # Reload the updated dataset
        today = date.today()
        st.write("NOAA Monthly Data Updated on {}".format(str(today)))

        # Now the logic is to dowload the data and save is that data will be the environment 
        # Next time someone has to open they do not have to run this commonad 
        
else:
    
    noaa= pd.read_csv("NOAA.csv")








    


st.session_state["my_input"] = df
st.session_state["noaa"] = noaa
