from math import sin, cos, sqrt, atan2, radians

class Calculator:

    @staticmethod
    def gps_to_kmeters(long1, lat1, long2, lat2):
        """Converts gps longitudes and latitudes distance to meters

        Keyword arguments:
        long1 -- longitude for pos 1
        lat1 -- latitute for pos 1
        long2 -- longitude for pos 2
        lat2 -- latitude for pos 2
        """

        #approx radius of earth
        R = 6373.0

        long1 = radians(long1)
        lat1 = radians(lat1)
        long2 = radians(long2)
        lat2 = radians(lat2)

        dist_long = long2 - long1
        dist_lat = lat2 - lat1

        a = sin(dist_lat / 2)**2 + cos(lat1) * cos(lat2) * sin(dist_long)**2
        c = 2 * atan2(sqrt(a), sqrt(1 - a))

        dist = R * c

        return dist
