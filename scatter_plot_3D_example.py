# Import the necessary packages
from mdvtools.mdvproject import MDVProject
import os
import pandas as pd
import json

# Assuming a similar class exists for Scatter plots based on your structure
from scatter_plot_3D import ScatterPlot3D  # This should be your 3D scatter plot class

# Create a ScatterPlot3D instance
scatter_plot = ScatterPlot3D(
    title="max_x_pixels x max_y_pixels x min_x_pixels",
    params=["max_x_pixels", "max_y_pixels", "min_x_pixels"],
    size=[300, 300],
    position=[10, 10],
    default_color="#377eb8",
    brush="default",
    center=[0, 0, 0],
    on_filter="hide",
    radius=5,
    opacity=0.8,
    axis_scales=[1, 1, 1],
    camera={"distance": 37543.999999999956, "theta": -1.038, "phi": 0.261}
)

# Assuming set_color_scale and other specific methods are replaced or adapted for 3D scatter
# If similar functionalities exist for ScatterPlot3D, set them here
# Otherwise, remove or replace these methods with relevant ScatterPlot3D configurations

# Serve the project
p = MDVProject(os.path.expanduser('~/mdv/cillian'), delete_existing=True)

path_to_data = '/Users/maria/Documents/wellcome_human_gen_project/MDV-local/cillian/cellmetadata.csv'
df = pd.read_csv(path_to_data, low_memory=False)

p.add_datasource(path_to_data, df)

# Assuming the ScatterPlot3D instance stores its configuration similarly to HeatmapPlot
scatter_chart = json.loads(json.dumps(scatter_plot.plot_data, indent=2).replace("\\", ""))
scatter_view = {'initialCharts': {path_to_data: [scatter_chart]}}

p.set_view("Maria", scatter_view)
p.set_editable(True)
p.serve()
