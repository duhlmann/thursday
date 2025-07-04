import streamlit as st
import pandas as pd
streamclean = pd.read_csv("Thursday.csv", header=None).dropna(axis=1, how='all')
st.write(streamclean.head())

# Show column names in the app so we know what to use
st.write("Columns in CSV:", list(streamclean.columns))
