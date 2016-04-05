import mplleaflet
import json
import os
import matplotlib.pyplot as plt
import numpy as np
import mplleaflet

class MapView():
    ''' creates map to show the ambulance and the car '''


    def __init__(self):
        pass

    def plot_coordinates(self, longitude, latitude, color):
        '''Plot coordinates in map
        :param longitude:
        :param latitude:
        :param color: red or blue for ambulance or car
        :return:
        '''

        plt.hold(True)
        plt.plot(longitude, latitude, color)


    def show_map(self):
        '''Shows map
        :return:
        '''
        
        mplleaflet.show()


if __name__ == "__main__":
    map = MapView()
    map.plot_coordinates(-83,40,'rs')
