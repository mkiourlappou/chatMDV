# Import the necessary packages
from mdvtools.mdvproject import MDVProject
import os
import pandas as pd
import json

# Import the necessary classes
from scatter_plot import ScatterPlot


# Create a ScatterPlot instance
scatter_plot = ScatterPlot(
    title="Sample Scatter Plot",
    params=["CD103", "CD16"],
    size=[495, 417],
    position=[24, 11]
)
scatter_plot.set_default_color("#377eb8")
scatter_plot.set_brush("poly")
scatter_plot.set_opacity(0.8)
scatter_plot.set_radius(2)
scatter_plot.set_color_legend(display=True, position=[375, 1])
scatter_plot.set_axis_properties("x", {"label": "CD103", "textSize": 13, "tickfont": 10})
scatter_plot.set_axis_properties("y", {"label": "CD16", "textSize": 13, "tickfont": 10})


# Serve the project
p = MDVProject(os.path.expanduser('~/mdv/cillian'), delete_existing=True)

path_to_data = '/Users/maria/Documents/wellcome_human_gen_project/MDV-local/cillian/cellmetadata.csv'
df = pd.read_csv(path_to_data, low_memory=False)

p.add_datasource(path_to_data, df)

maria_chart = json.loads(json.dumps(scatter_plot.plot_data, indent=2).replace("\\",""))
maria_view = {'initialCharts': {path_to_data: [maria_chart]}}

p.set_view("Maria", maria_view)
p.serve()

