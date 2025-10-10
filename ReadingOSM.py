import osmnx as ox
import geopandas as gpd
import matplotlib.pyplot as plt


gdf = gpd.read_file("avigliano2.osm", layer='multipolygons')
buildings = gdf[gdf["building"].notnull()].copy()

print(buildings.other_tags)


buildings.plot(figsize=(8, 8))
plt.title("Buildings in Avigliano")
plt.show()