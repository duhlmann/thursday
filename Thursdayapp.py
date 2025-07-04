import streamlit as st
import pandas as pd
import altair as alt

# Load the CSV with no renaming or cleanup
streamclean = pd.read_csv("Thursday.csv", header=None)

# Show raw CSV contents
st.title("🧪 RAW CSV PREVIEW")
st.write("Here is what the raw CSV looks like (first 15 rows):")
st.write(streamclean.head(15))

# Start Streamlit app
st.title("Daily Net Consumption")

# Slider for selecting day range
day_min, day_max = st.slider("Select Day Range", 1, 365, (1, 365))

# Filter the data by the selected day range
filtered_data = streamclean[(streamclean['Day'] >= day_min) & (streamclean['Day'] <= day_max)]

# Show debug info
st.write("Full data preview (first 10 rows):", streamclean.head(10))
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
