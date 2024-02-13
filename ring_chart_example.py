# Import the necessary packages
from mdvtools.mdvproject import MDVProject
import os
import pandas as pd
import json

# Import the RingChart class
from ring_chart import RingChart

# Create a RingChart instance
ring_chart = RingChart(
    title="label_drosophila",
    param="gene_name",
    size=[300, 300],
    position=[10, 10],
    id="dEVOKf"
)

# Configure the ring chart properties
ring_chart.set_legend("")  # Set the legend if any
ring_chart.set_axis_properties("x", {
    "textSize": 53,
    "label": "",  # Set the x-axis label if any
    "size": 40,
    "tickfont": 10
})

#ring_chart.set_hole_size(10)

# Serve the project
p = MDVProject(os.path.expanduser('~/mdv/phddata'), delete_existing=True)

# Assume you have a path to your data
path_to_data = '/Users/maria/Documents/wellcome_human_gen_project/MDV-local/phd_data/drosophila_protein_coding_screen.csv'
df = pd.read_csv(path_to_data, low_memory=False)

# Add data source
p.add_datasource(path_to_data, df)

# Convert the ring chart data to JSON and clean it
ring_chart_data = json.loads(json.dumps(ring_chart.plot_data, indent=2).replace("\\", ""))
ring_view = {'initialCharts': {path_to_data: [ring_chart_data]}}

# Set the view and serve the project
p.set_view("Maria", ring_view)
p.set_editable(True)
p.serve()
