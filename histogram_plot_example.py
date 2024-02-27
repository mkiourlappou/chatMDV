from mdvtools.mdvproject import MDVProject
import os
import pandas as pd
import json

from histogram_plot import HistogramPlot

# Create a HistogramPlot instance
histogram_plot = HistogramPlot(
    title="PANCK",
    param="PANCK",
    bin_number=20,
    display_min=0,
    display_max=62442.035,
    size=[792, 472],
    position=[10, 10]
)

histogram_plot.set_x_axis(size=30, label="PANCK", textsize=13, tickfont=10)
histogram_plot.set_y_axis(size=45, label="frequency", textsize=13, tickfont=10, rotate_labels=False)

# Serve the project
p = MDVProject(os.path.expanduser('~/mdv/cillian'), delete_existing=True)

path_to_data = '/Users/maria/Documents/wellcome_human_gen_project/MDV-local/cillian/cellmetadata.csv'
df = pd.read_csv(path_to_data, low_memory=False)

p.add_datasource(path_to_data, df)

maria_chart = json.loads(json.dumps(histogram_plot.plot_data, indent=2).replace("\\",""))
maria_view = {'initialCharts': {path_to_data: [maria_chart]}}

p.set_view("Maria", maria_view)
p.set_editable(True)
p.serve()
