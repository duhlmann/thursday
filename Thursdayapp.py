import streamlit as st
import pandas as pd
import altair as alt

# Load the CSV, skipping first 2 rows, selecting columns 1 to 4
streamclean = pd.read_csv("Thursday.csv", skiprows=2, usecols=[1,2,3,4])

# Rename columns to simple names
streamclean.columns = ['Index', 'Date', 'Day', 'Net Consumption (kWh)']

# Drop the 'Index' column since we don't need it
streamclean = streamclean.drop(columns=['Index'])

# Convert 'Day' to integer (important for filtering)
streamclean['Day'] = streamclean['Day'].astype(int)

# Show app title and slider to select day range
st.title("Daily Net Consumption")
day_min, day_max = st.slider("Select Day Range", 1, 365, (1, 365))

# Filter data for selected day range
filtered_data = streamclean[(streamclean['Day'] >= day_min) & (streamclean['Day'] <= day_max)]

# Show number of rows after filtering
st.write(f"Number of rows after filtering: {len(filtered_data)}")

if len(filtered_data) == 0:
    st.write("No data available for the selected day range.")
else:
    # Create a line chart using Altair
    chart = alt.Chart(filtered_data).mark_line(point=True).encode(
        x='Day',
        y='Net Consumption (kWh)',
        tooltip=['Date', 'Day', 'Net Consumption (kWh)']
    ).properties(
        width=700,
        height=400,
        title='Net Consumption (kWh) by Day'
    )

    st.altair_chart(chart, use_container_width=True)
