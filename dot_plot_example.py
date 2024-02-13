from mdvtools.mdvproject import MDVProject
import os
import pandas as pd
import json

# Import the DotPlot class
from dot_plot import DotPlot

# Create a DotPlot instance with configuration based on the JSON
dot_plot = DotPlot(
    title="label_drosophila",
    params=["label_drosophila", "UTR3_extension", "UTR3_max_length", "UTR3_mean_length", "UTR3_min_length"],
    size=[592, 457],
    position=[10, 10]
)

# Configure the dot plot
dot_plot.set_axis_properties("x", {"label": "", "textSize": 13, "tickfont": 10})
dot_plot.set_axis_properties("y", {"label": "", "textSize": 13, "tickfont": 10})
dot_plot.set_axis_properties("ry", {"label": "", "textSize": 13, "tickfont": 10})
dot_plot.set_color_scale(log_scale=False)
dot_plot.set_color_legend(True, [40, 10])
dot_plot.set_fraction_legend(True, [0, 0])

# Set up and serve the MDV project
project_path = '~/mdv/my_dot_project'
p = MDVProject(os.path.expanduser(project_path), delete_existing=True)

data_path = '/Users/maria/Documents/wellcome_human_gen_project/MDV-local/phd_data/drosophila_protein_coding_screen.csv'
df = pd.read_csv(data_path, low_memory=False)

# Add data to the project
p.add_datasource(data_path, df)

# Convert plot data to JSON and setup the project view
chart_data = json.loads(json.dumps(dot_plot.plot_data, indent=2).replace("\\", ""))
view_config = {'initialCharts': {data_path: [chart_data]}}

# Configure and serve the project
p.set_view("default", view_config)
p.set_editable(True)
p.serve()
