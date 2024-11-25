This project visualizes the Bigfoot sightings dataset using Altair and Vega-Lite. The data is collected from various sources and aims to provide an interactive visualization of where Bigfoot has been reportedly sighted.

- **bfro_reports_fall2022.csv**: The original dataset containing the Bigfoot sightings.
- **bigfoot_sightings.json**: The Vega-Lite JSON file generated using Altair, which can be used to embed the chart in a webpage.
- **bigfoot_sightings_chart.py**: Python script used to create the visualization.

To run this project, you need the following Python packages:

- `pandas`
- `altair`
- `vega_datasets`

You can install these packages using the following command:

```sh
pip install pandas altair vega_datasets
```

To generate the visualization, run the following command:

```sh
python bigfoot_sightings_chart.py
```

This will create a JSON file (`bigfoot_sightings.json`) that contains the visualization data, which can be used to embed the chart in a website.

To embed the chart in a website, you can use the following HTML code snippet:

```html
<div id="vis"></div>
<script src="https://cdn.jsdelivr.net/npm/vega@5"></script>
<script src="https://cdn.jsdelivr.net/npm/vega-lite@5"></script>
<script src="https://cdn.jsdelivr.net/npm/vega-embed@6"></script>
<script type="text/javascript">
  vegaEmbed('#vis', '/path/to/bigfoot_sightings.json').then(function(result) {
    // Visualization successfully embedded
  }).catch(console.error);
</script>
```

Replace `/path/to/bigfoot_sightings.json` with the correct path to your JSON file.


This project is licensed under the MIT License.
