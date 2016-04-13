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
        c = atan2(sqrt(a), sqrt(1 - a))

        dist = R * c

        return dist

    @staticmethod
    def speed(long1, lat1, long2, lat2, time_seconds):
        """Converts gps longitudes and latitudes and time beteen to 
        determine speed

        Keyword arguments:
        long1 -- longitude for old
        lat1 -- latitute for old
        long2 -- longitude for new
        lat2 -- latitude for new
        time_seconds
        """
        print(time_seconds)
        distance = Calculator.gps_to_kmeters(long1, lat1, long2, lat2)
        if time_seconds == 0:
            return 0
        speed = distance/(time_seconds/(60*60))

        return speed

    @staticmethod
    def time_to_intersection(distance, ambu_speed, car_speed):
        '''Calculates how much time is approximately left until the vehciles
        intersect. Returns the time in minutes.

        Keyword arguments:
        distance -- distance between vehciles in kms
        ambu_speed -- The ambulances current speed
        car_speed -- The cars current speed
        '''

        if ambu_speed - car_speed <= 0:
            return 0

        return (distance/(ambu_speed - car_speed))*60
