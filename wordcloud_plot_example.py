# wordcloud_plot_example.py

# Import the necessary packages
from mdvtools.mdvproject import MDVProject
import os
import pandas as pd
import json

# Import the necessary classes
from wordcloud_plot import WordcloudPlot

# Create a WordcloudPlot instance
wordcloud_plot = WordcloudPlot(
    title="sample_id",
    param="sample_id",
    wordSize=20,
    size=[502, 443],
    position=[10, 10]
)

wordcloud_plot.set_axis_properties("x", {"textSize": 13, "tickfont": 10})

# Serve the project
p = MDVProject(os.path.expanduser('~/mdv/cillian'), delete_existing=True)

path_to_data = '/Users/maria/Documents/wellcome_human_gen_project/MDV-local/cillian/cellmetadata.csv'
df = pd.read_csv(path_to_data, low_memory=False)

p.add_datasource(path_to_data, df)

maria_chart = json.loads(json.dumps(wordcloud_plot.plot_data, indent=2).replace("\\",""))
maria_view = {'initialCharts': {path_to_data: [maria_chart]}}

p.set_view("Maria", maria_view)
p.set_editable(True)
p.serve()
