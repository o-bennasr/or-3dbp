import pulp
import py3dbp
import numpy as np
import plotly.graph_objs as go
import streamlit as st


"""
MIP modelisation solving:

min  unused space

s.t. each box assigned to exactly one used bin
     each box within the limits of the bin
     the total weight of the boxes inside a ULD ≤ maximum capacity
     orthogonal placement
     no overlap
     orientation constraints
     special shape of the ULDS
     stability
     fragility
     weight distribution.

Source: https://orbi.uliege.be/bitstream/2268/159225/1/itor3.pdf
"""


st.title("Visualizing A container")


###
"""
Upload your load as a csv file
"""

w = st.file_uploader("Upload a CSV file", type="csv")

if w:
    import pandas as pd

    data = pd.read_csv(w)
    st.write(data)

st.header("Container")

x, y, z = np.random.multivariate_normal(np.array([0, 0, 0]), np.eye(3), 400).transpose()

trace1 = go.Scatter3d(
    x=x,
    y=y,
    z=z,
    mode="markers",
    marker=dict(
        size=12,
        color=z,  # set color to an array/list of desired values
        colorscale="Viridis",  # choose a colorscale
        opacity=0.8,
    ),
)

data = [trace1]
layout = go.Layout(margin=dict(l=0, r=0, b=0, t=0))
fig = go.Figure(data=data, layout=layout)

st.write(fig)

