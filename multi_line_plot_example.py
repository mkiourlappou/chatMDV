from mdvtools.mdvproject import MDVProject
import os
import pandas as pd
import json

from multi_line_plot import MultiLinePlot

# Create a MultiLinePlot instance
multi_line_plot = MultiLinePlot(
    title="PANCK",
    params=["PANCK", "sample_id"],
    size=[925, 502],
    position=[199, 18]
)

multi_line_plot.set_x_axis(label="PANCK", size=30, textsize=13, tickfont=10)
multi_line_plot.set_y_axis(label="density", size=45, textsize=13, tickfont=10)
multi_line_plot.set_bandwidth(0.1)
multi_line_plot.set_intervals(40)
multi_line_plot.set_scaletrim("0.001")
multi_line_plot.set_color_legend(True, [744, 18])

# Serve the project
p = MDVProject(os.path.expanduser('~/mdv/cillian'), delete_existing=True)

path_to_data = '/Users/maria/Documents/wellcome_human_gen_project/MDV-local/cillian/cellmetadata.csv'
df = pd.read_csv(path_to_data, low_memory=False)

p.add_datasource(path_to_data, df)

maria_chart = json.loads(json.dumps(multi_line_plot.plot_data, indent=2).replace("\\",""))
maria_view = {'initialCharts': {path_to_data: [maria_chart]}}

p.set_view("Maria", maria_view)
p.set_editable(True)
p.serve()
