from mdvtools.mdvproject import MDVProject
import os
import pandas as pd
import json

# Import the BoxPlot class
from box_plot import BoxPlot

# Create a BoxPlot instance
box_plot = BoxPlot(
    title="label_drosophila x UTR3_extension",
    params=["label_drosophila", "UTR3_extension"],
    size=[509, 555],
    position=[181, 0]
)

# Configure the box plot
box_plot.set_axis_properties("x", {"label": "label_drosophila", "textSize": 13, "tickfont": 10})
box_plot.set_axis_properties("y", {"label": "UTR3_extension", "textSize": 13, "tickfont": 10})
box_plot.set_default_color("black")
box_plot.set_opacity(0.8)
box_plot.set_tooltip(False)
box_plot.set_color_legend(True, [45, 10])

# Set up and serve the MDV project
project_path = '~/mdv/phddata'
p = MDVProject(os.path.expanduser(project_path), delete_existing=True)

data_path = '/Users/maria/Documents/wellcome_human_gen_project/MDV-local/phd_data/drosophila_protein_coding_screen.csv'
df = pd.read_csv(data_path, low_memory=False)

# Add data to the project
p.add_datasource(data_path, df)

# Convert plot data to JSON and setup the project view
chart_data = json.loads(json.dumps(box_plot.plot_data, indent=2).replace("\\", ""))
view_config = {'initialCharts': {data_path: [chart_data]}}

# Configure and serve the project
p.set_view("Maria", view_config)
p.set_editable(True)
p.serve()
