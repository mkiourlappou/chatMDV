from mdvtools.mdvproject import MDVProject
import os
import pandas as pd
import json
from sankey_plot import SankeyPlot

# Create a SankeyPlot instance
sankey_plot = SankeyPlot(
    title="",
    params=["image_id", "image_id"],
    size=[370, 405],
    position=[10, 10]
)

sankey_plot.set_axis_properties("y", {"size": 25, "textSize": 15, "label": "image_id", "tickfont": 10})
sankey_plot.set_axis_properties("ry", {"size": 25, "textSize": 15, "label": "image_id", "tickfont": 10})

# Serve the project
p = MDVProject(os.path.expanduser('~/mdv/cillian'), delete_existing=True)

path_to_data = '/Users/maria/Documents/wellcome_human_gen_project/MDV-local/cillian/cellmetadata.csv'
df = pd.read_csv(path_to_data, low_memory=False)

p.add_datasource(path_to_data, df)

maria_chart = json.loads(json.dumps(sankey_plot.plot_data, indent=2).replace("\\",""))
maria_view = {'initialCharts': {path_to_data: [maria_chart]}}

p.set_view("Maria", maria_view)
p.set_editable(True)
p.serve()
