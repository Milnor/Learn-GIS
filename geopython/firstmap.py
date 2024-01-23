import geopandas as gpd
import matplotlib.pyplot as plt

# OpenStreetMap API to query geodata
import osmnx as ox


#https://geopandas.org/en/stable/docs/user_guide/mapping.html
#chicago = geopandas.read_file(geodatasets.get_path("geoda.chicago_commpop"))
#groceries = geopandas.read_file(geodatasets.get_path("geoda.groceries"))

# https://geopandas.org/en/stable/docs/reference/api/geopandas.read_file.html#geopandas.read_file
world = gpd.read_file("DoS_LSIB_v11_3_19Dec2023\DoS_LSIB_v11_3_19Dec2023\data\DoS_LSIB_v11_3_19Dec2023.shp")
#world.plot(column="COUNTRY1", legend=False, cmap='OrRd')

print(f"type(world) = {type(world)}")
print(f"world.info() = {world.info()}")

# this should work, but neither this nor set_axis_off() is defined??
#world.axes("off")

# Large Scale International Boundaries
# https://data.geodata.state.gov/LSIB.zip


# https://www.tomasbeuzen.com/python-for-geospatial-analysis/chapters/chapter1_intro-to-spatial.html
world.plot(edgecolor="0.2", figsize=(10, 8))
plt.title("Countries on Earth")

# https://stackoverflow.com/questions/35484458/how-to-export-to-pdf-a-graph-based-on-a-pandas-dataframe
plt.savefig('myfile.pdf')   


## Lots of good resources here:
# https://forrest.nyc/75-geospatial-python-and-spatial-data-science-resources-and-guides/