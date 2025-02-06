import osmnx as ox
import pandas as pd

# Define starting location (latitude, longitude)
location_point = (-23.5505, -46.6333)  # São Paulo, Brazil

# Get street network within 2 km radius
G = ox.graph_from_point(location_point, dist=100, network_type="walk")

# Get all nodes (street corners)
nodes, _ = ox.graph_to_gdfs(G, nodes=True, edges=True)

# Extract latitude & longitude
nodes_df = nodes[['y', 'x']].reset_index()
nodes_df.columns = ['node_id', 'latitude', 'longitude']

# Add elevation data (requires Google API key)
api_key = "AIzaSyDQohTawlN9oGc-Ryxb1HNEorc811UIxOA"  # Replace with your actual API key

G = ox.elevation.add_node_elevations_google(G, api_key=api_key)

# Extract elevation for each node correctly
nodes_df = ox.convert.graph_to_gdfs(G, nodes=True, edges=False)

# Save results to a CSV
nodes_df.to_csv("street_corners.csv", index=False)

# # Display the first few rows
# print(nodes_df.head())