# Import the necessary packages
from mdvtools.mdvproject import MDVProject
import os
import pandas as pd
import json

# Import the necessary `classes`
from abundance_box_plot import AbundanceBoxPlot  # Adjusted from HeatmapPlot

# Create an AbundanceBoxPlot instance
abundance_box_plot = AbundanceBoxPlot(
    title="SAMPLE_10",
    params=["image_id", "roi_id", "sample_id"],  # Adjust as necessary based on your actual data
    size=[615, 557],
    position=[341, 49],
    id="tGa0CF"  # Example ID, change as needed
)

# Customize the box plot with additional settings from views.json
abundance_box_plot.set_x_axis([""], "")  # x-axis labels and title (empty as per views.json)
abundance_box_plot.set_y_axis(["% abundance SAMPLE_10"], "% abundance SAMPLE_10")  # y-axis labels and title
# Note: Additional customization like color, tooltip, method might be added here if applicable

# Serve the project
p = MDVProject(os.path.expanduser('~/mdv/cillian'), delete_existing=True)

path_to_data = '/Users/maria/Documents/wellcome_human_gen_project/MDV-local/cillian/cellmetadata.csv'
df = pd.read_csv(path_to_data, low_memory=False)

p.add_datasource(path_to_data, df)

# Convert plot data to JSON format and integrate into MDV view
abundance_chart = json.loads(json.dumps(abundance_box_plot.plot_data, indent=2).replace("\\", ""))
abundance_view = {'initialCharts': {path_to_data: [abundance_chart]}}

p.set_view("Maria", abundance_view)
p.set_editable(True)
p.serve()

