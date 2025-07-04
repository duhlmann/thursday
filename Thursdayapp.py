import streamlit as st
import pandas as pd

# Just read the raw CSV without any processing
df = pd.read_csv("Thursday.csv", header=None)

# Show raw CSV structure
st.title("🧪 Raw Thursday.csv Data Preview")
st.write("First 15 rows of the raw file:")
st.write(df.head(15))

# Show number of rows and columns
st.write("Shape of raw CSV:", df.shape)
