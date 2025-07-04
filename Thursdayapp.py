import streamlit as st
import pandas as pd
import altair as alt

# Manually name columns when loading CSV
column_names = ['Index', 'Dates', 'Day', 'Net Consumption (kWh)', 'Extra1', 'Extra2', 'Extra3']
streamclean = pd.read_csv("Thursday.csv", header=None, names=column_names)

# Drop unused columns
streamclean = streamclean.drop(columns=['Index', 'Extra1', 'Extra2', 'Extra3'])

# Convert 'Day' to int for filtering
streamclean['Day'] = pd.to_numeric(streamclean['Day'], errors='coerce').fillna(0).astype(int)

st.title("Daily Net Consumption")

# Slider for selecting day range
day_min, day_max = st.slider("Select Day Range", min_value=1, max_value=365, value=(1, 365))

# Filter data by day range
filtered_data = streamclean[(streamclean['Day'] >= day_min) & (streamclean['Day'] <= day_max)]

# Altair line chart
chart = alt.Chart(filtered_data).mark_line(point=True).encode(
    x=alt.X('Day', title='Day of Year'),
    y=alt.Y('Net Consumption (kWh)', title='Net Consumption (kWh)'),
    tooltip=['Dates', 'Net Consumption (kWh)']
).properties(
    width=700,
    height=400,
    title="Net Consumption over Selected Days"
)

st.altair_chart(chart, use_container_width=True)
