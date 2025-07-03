import streamlit as st
import pandas as pd
import altair as alt


streamclean = pd.read_csv("util.csv")
# Sidebar title
st.sidebar.title("Settings")

# Sidebar input example: select a month to filter
month_options = ['All Months', 'January', 'February', 'March', 'April', 'May', 'June', 
                 'July', 'August', 'September', 'October', 'November', 'December']

selected_month = st.sidebar.selectbox("Select Month", month_options)

# Load your data (replace with your real data loading)
# streamclean = pd.read_csv('your_data.csv')
# For now, assume streamclean is already loaded

# Filter data if a specific month is selected
if selected_month != 'All Months':
    filtered_data = streamclean[streamclean['Month'] == selected_month]
else:
    filtered_data = streamclean

# Your chart code here, using filtered_data instead of streamclean
zoom = alt.selection_interval(encodings=['x'])

month_order = ['January', 'February', 'March', 'April', 'May', 'June', 
               'July', 'August', 'September', 'October', 'November', 'December']

filtered_data['Month'] = pd.Categorical(filtered_data['Month'], categories=month_order, ordered=True)

faceted_chart = alt.Chart(filtered_data).mark_line(point=True).encode(
    x=alt.X('Day:Q', title='Day of Month', axis=alt.Axis(tickCount=10)),
    y=alt.Y('Net Consumption (kWh):Q', title='Net Consumption (kWh)'),
    tooltip=[
        alt.Tooltip('Dates:T', title='Date'),
        alt.Tooltip('Net Consumption (kWh):Q', title='Consumption (kWh)'),
    ]
).add_params(
    zoom
).properties(
    width=350,
    height=200,
    title='Daily Net Consumption by Month (Zoom & Pan Enabled)'
).facet(
    column=alt.Column('Month:N', sort=month_order, header=alt.Header(labelAngle=0, labelFontSize=14))
).resolve_scale(
    y='shared',
    x='shared'
)

st.altair_chart(faceted_chart, use_container_width=True)











