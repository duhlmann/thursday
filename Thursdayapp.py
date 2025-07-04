import streamlit as st
import pandas as pd

column_names = ['Index', 'Dates', 'Day', 'Net Consumption (kWh)', 'Extra1', 'Extra2', 'Extra3']

streamclean = pd.read_csv("Thursday.csv", header=None, names=column_names)

# Drop 'Index' and any 'Extra' columns (empty columns)
streamclean = streamclean.drop(columns=['Index', 'Extra1', 'Extra2', 'Extra3'])

st.write("Columns found in CSV after renaming and dropping:", list(streamclean.columns))
st.write(streamclean.head())
