
---
name: Bigfoot Report Analysis Project
tools: [Python, Pandas, Altair]
image: assets/pngs/bigfoot_analysis.png
description: This project analyzes Bigfoot sighting data using Python and creates interactive visualizations for exploratory data analysis!
custom_js:
  - pandas.min
  - altair.min
---

# Bigfoot Sighting Data Analysis

This project delves into the dataset of Bigfoot sightings to uncover patterns and trends. The analysis employs Python for data preprocessing and Altair for creating insightful visualizations. Explore the geographical and temporal distribution of sightings through interactive charts and maps.

<vegachart schema-url="/assets/json/geographical_chart.json" style="width: 100%"></vegachart>
<vegachart schema-url="/assets/json/temporal_chart.json" style="width: 100%"></vegachart>

---

## Data & Methods

Below are links to both the raw data and the analysis code, conveniently provided as buttons for direct access:

<div class="left">
{% include elements/button.html link="https://github.com/loveandpeace2004/loveandpeace2004.github.io/blob/main/bfro_reports_fall2022.csv" text="The Data" %}
</div>

<div class="right">
{% include elements/button.html link="https://github.com/loveandpeace2004/loveandpeace2004.github.io/blob/main/Workbook.ipynb" text="The Analysis" %}
</div>

---

## About the Project

The geographical chart highlights hotspots for Bigfoot sightings across different regions, while the temporal chart reveals trends over the years. Both visualizations are built with Altair, leveraging its interactive features to allow detailed exploration of the dataset.

For more information, check out the analysis notebook linked above!
