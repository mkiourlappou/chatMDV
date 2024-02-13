
from mdvtools.mdvproject import MDVProject
import pandas as pd
import json
import os

# Assuming the BoxPlot class is suitable for showing the distribution, we'll use it.
from box_plot import BoxPlot

# Create a BoxPlot instance to visualize the distribution of 'label_drosophila' and 'UTR3_extension'
box_plot = BoxPlot(
    title="Distribution of label_drosophila and UTR3_extension",
    params=["label_drosophila", "UTR3_extension"],
    size=[600, 400],  # Adjusted size for better visibility
    position=[100, 50]  # Adjusted position
)

# Configure the box plot with appropriate settings
box_plot.set_axis_properties("x", {"label": "Drosophila Label", "textSize": 12, "tickfont": 10})
box_plot.set_axis_properties("y", {"label": "UTR3 Extension", "textSize": 12, "tickfont": 10})
box_plot.set_default_color("blue")  # Use blue for better visual distinction
box_plot.set_opacity(0.75)  # Slightly less opaque
box_plot.set_tooltip(True)  # Enable tooltips for more interactive data exploration
box_plot.set_color_legend(True, [40, 20])  # Enable color legend with adjusted position

# Setup the MDV project (Assuming a similar setup as in the example)
project_path = '~/mdv/phddata'  # Placeholder path
p = MDVProject(os.path.expanduser(project_path), delete_existing=True)

# Use the path to the CSV file you uploaded
data_path = '/Users/maria/Documents/wellcome_human_gen_project/MDV-local/phd_data/drosophila_protein_coding_screen.csv'
df = pd.read_csv(data_path, low_memory=False)

# Add data to the project
p.add_datasource("Drosophila Data", df)

# Convert plot data to JSON for the MDV project configuration
chart_data = json.loads(json.dumps(box_plot.plot_data, indent=2).replace("\\", ""))
view_config = {'initialCharts': {"Drosophila Data": [chart_data]}}

# Configure and serve the project
p.set_view("Your Name", view_config)
p.set_editable(True)
p.serve()
