from bokeh.plotting import figure, show, output_file
from bokeh.models import ColumnDataSource, HoverTool

# this is our visualizer file that we tend to need to visualize our results after

class Visualizer:
    def plot_data(self, mapping_results, title="Test Data Mapping Results"):
        output_file("mapping_results.html")  # Save the plot as an HTML file

        source = ColumnDataSource(data={
            'x': [res[0] for res in mapping_results],
            'y': [res[1] for res in mapping_results],
            'function': [res[2] for res in mapping_results],
            'deviation': [res[3] for res in mapping_results],
            'color': ['green' if res[2] != 'None' else 'red' for res in mapping_results]
        })

        p = figure(title=title, x_axis_label='x', y_axis_label='y', tools="pan,wheel_zoom,box_zoom,reset,hover,save")
        p.circle('x', 'y', color='color', legend_field='function', fill_alpha=0.6, size=10, source=source)

        hover = p.select(dict(type=HoverTool))
        hover.tooltips = [
            ("x", "@x"),
            ("y", "@y"),
            ("Function", "@function"),
            ("Deviation", "@deviation")
        ]

        p.legend.title = 'Matched Function'
        show(p)
