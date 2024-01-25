import geopandas as gpd
import matplotlib.pyplot as plt

# OpenStreetMap API to query geodata
import osmnx as ox
# TODO: use it to add cities or remove

# Initially I used the State Department's LSIB shapefile, but it only included land boundaries, not coastline.
#world = gpd.read_file("DoS_LSIB_v11_3_19Dec2023\DoS_LSIB_v11_3_19Dec2023\data\DoS_LSIB_v11_3_19Dec2023.shp")
# ESRI's World_Countries_Generalized shapefile proved better suited to this project
world = gpd.read_file("World_Countries_Generalized\World_Countries_Generalized.shp")

# Add a VISIT column to GeoDataFrame that by default says I've never visited the country
world['VISIT'] = 0

# this gives columns, not helpful for what I'm trying to do
# for record in world:
#    print(record)

# *this* is how you iterate records
# index 2 was country name and 3 was ISO code
#for record in world.itertuples():
#    print(record[0], record[2], record[3])

# TODO: should probably be an Enum; find solution that works with map legend
# length of stay
0 # never visited (airports don't count)
1 # a day or less
2 # more than one day to a couple weeks
3 # lived there a few weeks to several months
4 # lived there for years

# Manually specify how long I VISITed each country
world.loc[22, 'VISIT'] = 2  # BZ Belize
world.loc[41, 'VISIT'] = 2  # CA Canada
world.loc[47, 'VISIT'] = 4  # CN China
world.loc[108, 'VISIT'] = 1 # IE Ireland
world.loc[110, 'VISIT'] = 3 # IL Israel
world.loc[111, 'VISIT'] = 2 # IT Italy
world.loc[113, 'VISIT'] = 3 # JP Japan
world.loc[115, 'VISIT'] = 2 # JO Jordan
world.loc[143, 'VISIT'] = 2 # MX Mexico
world.loc[156, 'VISIT'] = 2 # NL Netherlands
world.loc[211, 'VISIT'] = 3 # KR South Korea
world.loc[213, 'VISIT'] = 2 # ES Spain
world.loc[223, 'VISIT'] = 2 # TH Thailand
world.loc[230, 'VISIT'] = 2 # TR Turkiye
world.loc[237, 'VISIT'] = 3 # GB United Kingdom
world.loc[238, 'VISIT'] = 4 # US United States
world.loc[244, 'VISIT'] = 1 # VA Vatican City

plt.title("Countries Visited")

# Omit Southern Hemisphere since I've never been there
fig, ax = plt.subplots(figsize=(24, 16))
world.plot(edgecolor="0.1", ax=ax, column="VISIT", legend=True, cmap='BuPu', categorical=True)
ax.set_xlim(-150, 150)
ax.set_ylim(0, 75)


# TODO: add cities, or remove this part
# ga = ox.geocode_to_gdf("Georgia, USA")
#ga.plot(color="tomato") # I want to plot on top, not replace the main world plot

plt.savefig('CountriesVisited.pdf')   


'''
References
* https://forrest.nyc/75-geospatial-python-and-spatial-data-science-resources-and-guides/
* https://geopandas.org/en/stable/docs/user_guide/mapping.html
* https://stackoverflow.com/questions/35484458/how-to-export-to-pdf-a-graph-based-on-a-pandas-dataframe
* https://stackoverflow.com/questions/58014498/how-to-restrict-a-geopandas-plot-by-coordinates
* https://www.tomasbeuzen.com/python-for-geospatial-analysis/chapters/chapter1_intro-to-spatial.html

Data Sets
* ESRI, World Countries Generalized, https://hub.arcgis.com/datasets/esri::world-countries-generalized/about
* US State Department, Large Scale International Boundaries, https://data.geodata.state.gov/LSIB.zip
'''