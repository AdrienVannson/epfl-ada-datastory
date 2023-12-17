import numpy as np
import plotly.express as px

fig = px.scatter(x=range(100), y=np.sin(np.arange(100) / 10))
fig.write_html("_includes/graph.html")