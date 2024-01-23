import geopandas
import matplotlib.pyplot as plt

#https://geopandas.org/en/stable/docs/user_guide/mapping.html
#chicago = geopandas.read_file(geodatasets.get_path("geoda.chicago_commpop"))
#groceries = geopandas.read_file(geodatasets.get_path("geoda.groceries"))

# https://geopandas.org/en/stable/docs/reference/api/geopandas.read_file.html#geopandas.read_file
world = geopandas.read_file("DoS_LSIB_v11_3_19Dec2023\DoS_LSIB_v11_3_19Dec2023\data\DoS_LSIB_v11_3_19Dec2023.shp")
world.plot(column="COUNTRY1", legend=False, cmap='OrRd')

# Large Scale International Boundaries
# https://data.geodata.state.gov/LSIB.zip

# https://stackoverflow.com/questions/35484458/how-to-export-to-pdf-a-graph-based-on-a-pandas-dataframe
plt.savefig('myfile.pdf')   