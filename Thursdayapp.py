import streamlit as st
import pandas as pd
import altair as alt

# Load the CSV with no header and assign your own column names
column_names = ['Index', 'Dates', 'Day', 'Net Consumption (kWh)', 'Extra1', 'Extra2', 'Extra3']
streamclean = pd.read_csv("Thursday.csv", header=None, names=column_names)

# Drop unused columns
streamclean = streamclean.drop(columns=['Index', 'Extra1', 'Extra2', 'Extra3'])

# Convert 'Day' safely to integers
streamclean['Day'] = pd.to_numeric(streamclean['Day'], errors='coerce').fillna(0).astype(int)

# Start Streamlit app
st.title("Daily Net Consumption")

# Slider for selecting day range
day_min, day_max = st.slider("Select Day Range", 1, 365, (1, 365))

# Filter the data by the selected day range
filtered_data = streamclean[(streamclean['Day'] >= day_min) & (streamclean['Day'] <= day_max)]

# Show debug info
st.write("All unique Day values in dataset:", streamclean['Day'].unique())
# Show chart only if there is data
if not filtered_data.empty:
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
else:
    st.warning("No data available for the selected day range.")
