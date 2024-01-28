# Notes on Geographic Information Systems

## Data Types

### Vector Data
* Collection of locations/vertices that define one of three shapes
    - **Point**, individual **x, y** or **x, y, z** location
    - **Line**, composed of at least two connected points
        * Do not need to be straight lines, e.g. roads and streams
    - **Polygon**, three or more vertices that are connected and **closed**
        * e.g. building boundaries and lakes
* Common format is **Shapefile**

### Raster Data
* A Matrix of pixels/cells; each cell represents a small area and contains a value representing... *something*
* Common format is **GeoTIFF (.tif)**
## File Types

### Shapefile
* Stores vector data
* A collection of three or more files including at least these three:
    - *filename.shp* - main file that stores shape geometries
    - *filename.shx* - index of how the geometries above relate to one another
    - *filename.dbf* - attributes of each record
* Can only store one type of shape, i.e. all points, all lines, or all polygons
* Others -- see notes from Coursera class and add here...

### Geojson
* Stores vector data

## Python Libraries

### geopandas
* Built off of `shapely` and `pandas`
* Two main classes for spatial data manipulation:
    - *GeoSeries**, akin to `pandas` series
    - *GeoDataFrame**, akin to `pandas` dataframe
* Usually imported using `gpd` alias, i.e. `import geopandas as gpd`

### rasterio
* Used for working with raster data

## References
* Tomas Beuzen. [Python for Geospatial Analysis](https://www.tomasbeuzen.com/python-for-geospatial-analysis/chapters/chapter1_intro-to-spatial.html), 2021.
    - Beautiful text that ties theory to practice using `geopandas`

## Links for University of Helsinki class
* https://geo-python-site.readthedocs.io/en/latest/lessons/L1/overview.html
* https://github.com/Geo-Python-2023/exercise-1-Milnor
* Jupyter notebook app crashed...