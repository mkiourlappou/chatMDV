# Import the necessary packages
from mdvtools.mdvproject import MDVProject
import os
import pandas as pd
import json

# Import the necessary `classes`
from density_scatter_plot import DensityScatterPlot

# Create a DensityScatterPlot instance based on the attributes specified in views.json
density_scatter_plot = DensityScatterPlot(
    title="CD103 x CD20",
    params=["CD103", "CD20", "sample_id"],
    size=[698, 556],
    position=[10, 10]
)

# Set additional properties for the plot as per the JSON file
density_scatter_plot.set_x_axis(label="CD103", size=30, textsize=13, tickfont=10)
density_scatter_plot.set_y_axis(label="CD20", size=45, textsize=13, tickfont=10, rotate_labels=False)
#density_scatter_plot.set_contour_details(bandwidth=10.64, intensity=0.7, opacity=1)
density_scatter_plot.set_visuals(
    default_color="#377eb8",
    radius=2,
    opacity=0.8,
    log_color_scale=True,
    fallback_on_zero=True,
    background_color="white",
    bandwidth=10.64,
    intensity=0.7,
    opacity_cnt=1
)

# Serve the project
p = MDVProject(os.path.expanduser('~/mdv/cillian'), delete_existing=True)

path_to_data = '/Users/maria/Documents/wellcome_human_gen_project/MDV-local/cillian/cellmetadata.csv'
df = pd.read_csv(path_to_data, low_memory=False)

p.add_datasource(path_to_data, df)

# Convert plot data to format compatible with MDVProject
maria_chart = json.loads(json.dumps(density_scatter_plot.plot_data, indent=2).replace("\\", ""))
maria_view = {'initialCharts': {path_to_data: [maria_chart]}}

p.set_view("Maria", maria_view)
p.set_editable(True)
p.serve()
