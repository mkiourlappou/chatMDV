# Import the necessary packages
from mdvtools.mdvproject import MDVProject
import os
import pandas as pd
import json
import numpy as np

# Import the necessary classes
from scatter_plot import ScatterPlot

list_charts = []
# Create a ScatterPlot instance
parameter_pairs = [["halflife", "Isoform min length"], ["halflife", "Isoform max length"], ["halflife", "Isoform mean length"]]
initial_positions = [1, 1]
#for parameter_pair in parameter_pairs:
for i in range(0,len(parameter_pairs)):
    scatter_plot = ScatterPlot(
        title="Sample Scatter Plot",
        params=parameter_pairs[i],
        size=[631, 163],
        position= [x + y for x, y in zip(initial_positions, [k * i for k in [0, 180]])]
    )
    print(i)
    scatter_plot.set_default_color("#377eb8")
    scatter_plot.set_brush("poly")
    scatter_plot.set_opacity(0.8)
    scatter_plot.set_radius(2)
    scatter_plot.set_color_legend(display=True, position=[375, 1])
    scatter_plot.set_axis_properties("x", {"label": parameter_pairs[i][0], "textSize": 13, "tickfont": 10})
    scatter_plot.set_axis_properties("y", {"label": parameter_pairs[i][1], "textSize": 13, "tickfont": 10})

    maria_chart = json.loads(json.dumps(scatter_plot.plot_data, indent=2).replace("\\",""))
    list_charts.append(maria_chart)

# Serve the project
p = MDVProject(os.path.expanduser('~/mdv/phddata'), delete_existing=True)

path_to_data = '/Users/maria/Documents/wellcome_human_gen_project/MDV-local/phd_data/drosophila_protein_coding_screen.csv'
df = pd.read_csv(path_to_data, low_memory=False)
p.add_datasource(path_to_data, df)
maria_view = {'initialCharts': {path_to_data: list_charts}}


p.set_view("default", maria_view)
p.serve()

