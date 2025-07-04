import streamlit as st
import pandas as pd

streamclean = pd.read_csv("Thursday.csv")

st.write("Columns found in CSV:", list(streamclean.columns))
