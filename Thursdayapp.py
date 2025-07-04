import streamlit as st
import pandas as pd

streamclean = pd.read_csv("Thursday.csv", header=0, index_col=0)

st.write("Columns found in CSV:", list(streamclean.columns))
st.write(streamclean.head())

