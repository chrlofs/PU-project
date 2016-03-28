from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import numpy as np
# setup Lambert Conformal basemap.


class Carmap:
    '''
    making a map with basemap
    install basemap: http://gnperdue.github.io/yak-shaving/osx/python/matplotlib/2014/05/01/basemap-toolkit.html
    '''

    def __init__(self):

        self.m = Basemap(llcrnrlon=-93.7, llcrnrlat=28., urcrnrlon=-66.1, urcrnrlat=39.5,
              projection='lcc', lat_1=30., lat_2=60., lat_0=34.83158, lon_0=-98.)


    def plot(self, lon, lat, color):
        '''
        making plot at the map
        :param color: which color of the dot
        '''
        lon, lat = lon, lat # Location of Boulder
        # convert to map projection coords.
        # Note that lon,lat can be scalars, lists or numpy arrays.
        xpt, ypt = self.m(lon, lat)
        self.m.plot(xpt, ypt, color)    # plot a color dot there

    def show(self):
        self.m.bluemarble()  # map style
        plt.show()


if __name__ == '__main__':
    m = Carmap()
    m.plot(-83, 42, 'bo')
    m.plot(-80, 65, 'ro')
    m.show()
