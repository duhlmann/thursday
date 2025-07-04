import streamlit as st
import pandas as pd

df = pd.read_csv("Thursday.csv", header=None)

st.title("🧪 Raw Thursday.csv Data Preview - Text Version")
st.write("First 15 rows of the raw file as text:")

# Convert the first 15 rows to a string
raw_text = df.head(15).to_string(index=True)

st.text(raw_text)

st.write("Shape of raw CSV:", df.shape)
