import streamlit as st
import pandas as pd
import altair as alt

# Read CSV with header row, and skip the first unnamed column by using usecols
streamclean = pd.read_csv("Thursday.csv", usecols=["Dates", "Day", "Net Consumption (kWh)"])

# Convert 'Day' to integer (sometimes read as float)
streamclean['Day'] = streamclean['Day'].astype(int)

# Show first 5 rows to confirm
st.write("Data preview:")
st.write(streamclean.head())

# Title
st.title("Daily Net Consumption")

# Slider to select day range
day_min, day_max = st.slider("Select Day Range", 1, 365, (1, 365))

# Filter data for day range
filtered_data = streamclean[(streamclean['Day'] >= day_min) & (streamclean['Day'] <= day_max)]

# Create Altair line chart
chart = alt.Chart(filtered_data).mark_line(point=True).encode(
    x=alt.X('Day', title='Day of Year'),
    y=alt.Y('Net Consumption (kWh)', title='Net Consumption (kWh)'),
    tooltip=['Dates', 'Net Consumption (kWh)']
).properties(
    width=700,
    height=400,
    title="Net Consumption over Days"
)

# Show chart in Streamlit
st.altair_chart(chart, use_container_width=True)
