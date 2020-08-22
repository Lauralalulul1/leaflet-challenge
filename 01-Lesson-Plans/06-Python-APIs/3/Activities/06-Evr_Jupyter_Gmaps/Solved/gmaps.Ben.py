import gmaps
# Google developer API key
from config import gkey
# Access maps with unique API key
gmaps.configure(api_key=gkey)
# Create a list containing coordinates
coordinates = [
    (38.9822, 0-94.6708),
    (30.26, -97.74),
    (46.87, -96.78),
    (47.60, -122.33),
    (32.71, -117.16)
]
# Customize the size of the figure
figure_layout = {
    'width': '400px',
    'height': '300px',
    'border': '1px solid black',
    'padding': '1px',
    'margin': '0 auto 0 auto'
}
fig = gmaps.figure(layout=figure_layout)
# Assign the marker layer to a variable
markers = gmaps.marker_layer(coordinates)
# Add the layer to the map
fig.add_layer(markers)
fig