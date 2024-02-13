from mdvtools.mdvproject import MDVProject
import os
import pandas as pd
import json

# Import the StackedRowChart class
from stacked_row_plot import StackedRowChart

# Create a StackedRowChart instance with configuration from the JSON
stacked_row_chart = StackedRowChart(
    title="",
    params=["label_drosophila", "gene_name"],
    size=[959, 591],
    position=[142, 0]
)

# Configure the stacked row chart
stacked_row_chart.set_axis_properties("x", {"textSize": 13, "label": "", "tickfont": 10})
stacked_row_chart.set_axis_properties("y", {"textSize": 13, "label": "", "tickfont": 10})
stacked_row_chart.set_color_legend(False)

# Set up and serve the MDV project
project_path = '~/mdv/my_stacked_row_project'
p = MDVProject(os.path.expanduser(project_path), delete_existing=True)

data_path = '/Users/maria/Documents/wellcome_human_gen_project/MDV-local/phd_data/drosophila_protein_coding_screen.csv'
df = pd.read_csv(data_path, low_memory=False)

# Add data to the project
p.add_datasource(data_path, df)

# Convert plot data to JSON and setup the project view
chart_data = json.loads(json.dumps(stacked_row_chart.plot_data, indent=2).replace("\\", ""))
view_config = {'initialCharts': {data_path: [chart_data]}}

# Configure and serve the project
p.set_view("default", view_config)
p.set_editable(True)
p.serve()
