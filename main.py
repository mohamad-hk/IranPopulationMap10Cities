from mpl_toolkits.basemap import Basemap
import numpy as np
import matplotlib.pyplot as plt

from ExtractData import pre_processing_data

population_list, df = pre_processing_data()
fig = plt.figure()
ax = fig.add_axes([0.1, 0.1, 0.8, 0.8])

m = Basemap(llcrnrlon=44., llcrnrlat=24., urcrnrlon=62., urcrnrlat=40.,
            rsphere=(6378137.00, 6356752.3142),
            resolution='i', projection='merc',
            lat_0=30., lon_0=53., lat_ts=30.)

m.drawcoastlines()
m.fillcontinents()
m.drawcountries()

x, y = m(df["lon_decimal"].values, df["lat_decimal"].values)

m.scatter(x, y, color='red', marker='o', zorder=5, s=np.sqrt(population_list) * 0.3)



ax.set_title('Iran Population Map')

plt.show()
