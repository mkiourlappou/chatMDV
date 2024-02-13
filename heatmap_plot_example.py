# Import the necessary packages
from mdvtools.mdvproject import MDVProject
import os
import pandas as pd
import json

# Import the necessary `classes`
from heatmap_plot import HeatmapPlot


# Create a ScatterPlot instance
heatmap_plot = HeatmapPlot(
    title="Sample Heatmap Plot",
    params=["image_id", "CD10"],
    size=[495, 417],
    position=[24, 11]
)

heatmap_plot.set_color_scale({"log": False})
heatmap_plot.set_intensity_scale([0, 0.5, 1])
heatmap_plot.set_opacity(0.8)
heatmap_plot.set_color_range([0, 100])
heatmap_plot.set_tooltip(True)
heatmap_plot.set_method("mean")
heatmap_plot.set_axis_properties("x", {"label": "cell_id", "textSize": 13, "tickfont": 10})
heatmap_plot.set_axis_properties("y", {"label": "y", "textSize": 13, "tickfont": 10})


# Serve the project
p = MDVProject(os.path.expanduser('~/mdv/cillian'), delete_existing=True)

path_to_data = '/Users/maria/Documents/wellcome_human_gen_project/MDV-local/cillian/cellmetadata.csv'
df = pd.read_csv(path_to_data, low_memory=False)

p.add_datasource(path_to_data, df)

maria_chart = json.loads(json.dumps(heatmap_plot.plot_data, indent=2).replace("\\",""))
maria_view = {'initialCharts': {path_to_data: [maria_chart]}}

p.set_view("Maria", maria_view)
p.set_editable(True)
p.serve()

