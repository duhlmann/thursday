import streamlit as st
import pandas as pd
import altair as alt

streamclean = pd.read_csv("Thursday.csv")

st.write(streamclean.columns)

# Title of the app
st.title("Daily Net Consumption")

# Slider to select day range
day_min, day_max = st.slider("Select Day Range", 1, 365, (1, 365))

# Filter data based on selected days
filtered_data = streamclean[(streamclean['Day'] >= day_min) & (streamclean['Day'] <= day_max)]

# Create the line chart
chart = alt.Chart(filtered_data).mark_line(point=True).encode(
    x=alt.X('Day:Q', title='Day of Year'),
    y=alt.Y('Net Consumption (kWh):Q', title='Net Consumption (kWh)'),
    tooltip=['Dates:T', 'Net Consumption (kWh):Q']
).properties(
    width=700,
    height=400,
    title="Net Consumption over Days"
)

# Show the chart in Streamlit
st.altair_chart(chart, use_container_width=True)
