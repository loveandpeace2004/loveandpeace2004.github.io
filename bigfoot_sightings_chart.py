
import pandas as pd
import altair as alt

# 读取大脚怪目击事件数据
df = pd.read_csv('bfro_reports_fall2022.csv')

df.rename(columns={
    "latitude": "Latitude",
    "longitude": "Longitude",
    "state": "State",
    "date": "Date",
    "location_details": "Location Details"
}, inplace=True)

chart = alt.Chart(df).mark_circle(size=60).encode(
    x='Longitude',
    y='Latitude',
    color='State',
    tooltip=['Date', 'State', 'Location Details', 'Latitude', 'Longitude']
).interactive()

chart.properties(width='container').save("bigfoot_sightings.json")
