import numpy as np
import plotly.graph_objects as go

x_values = np.linspace(-np.pi,np.pi,1_000)
y_values = np.sin(
                3.2*np.pi*np.cos(x_values)
            )/(
                4*np.sin(0.8*np.pi*np.cos(x_values))
            )

fig = go.Figure([go.Scatter(x=x_values, y=y_values)])
fig.update_xaxes(title_text='Azimuthal Angle')
fig.update_yaxes(title_text='Array Factor')

fig.show()