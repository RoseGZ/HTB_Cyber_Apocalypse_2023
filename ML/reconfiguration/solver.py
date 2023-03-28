import Orange

# Load the Orange workflow from the .ows file
workflow = Orange.canvas.load_workflow("analysis.ows")

# Load the input data from the CSV file
data = Orange.data.Table("points.csv")

# Set the input data for the workflow
workflow.set_data(data)

# Display the output of the Scatter Plot widget
scatter_plot = workflow.widget(0)
scatter_plot_view = scatter_plot.create_container()
scatter_plot_view.show()

# Start the Orange GUI main loop
Orange.canvas.main_loop()
