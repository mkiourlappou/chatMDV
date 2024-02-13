# Import the necessary classes
from scatter_plot import ScatterPlot
from dot_plot import DotPlot

# Create a ScatterPlot instance
scatter_plot = ScatterPlot(
    title="Sample Scatter Plot",
    params=["umap_rna_harm_1", "umap_rna_harm_2"],
    size=[495, 417],
    position=[24, 11]
)
scatter_plot.set_default_color("#377eb8")
scatter_plot.set_brush("poly")
scatter_plot.set_opacity(0.8)
scatter_plot.set_radius(2)
scatter_plot.set_color_by("prot:tissue")
scatter_plot.set_color_legend(display=True, position=[375, 1])
scatter_plot.set_axis_properties("x", {"label": "umap_rna_harm_1", "textSize": 13, "tickfont": 10})
scatter_plot.set_axis_properties("y", {"label": "umap_rna_harm_2", "textSize": 13, "tickfont": 10})

# Output ScatterPlot JSON
print("ScatterPlot JSON:\n", scatter_plot.to_json())

# Create a DotPlot instance
dot_plot = DotPlot(
    title="Sample Dot Plot",
    params=[
        "prot:annotation",
        "logged_counts|S100A8(logged_counts)|2061",
        # ... other parameters ...
    ],
    size=[761, 413],
    position=[17, 435]
)
dot_plot.set_axis_properties("x", {"textSize": 13, "tickfont": 11, "rotate_labels": True})
dot_plot.set_axis_properties("y", {"textSize": 13, "tickfont": 11})
dot_plot.set_color_scale(log_scale=False)
dot_plot.set_color_legend(display=True, position=[622, 15])
dot_plot.set_fraction_legend(display=True, position=[622, 83])

# Output DotPlot JSON
print("\nDotPlot JSON:\n", dot_plot.to_json())
