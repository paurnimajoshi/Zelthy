import math
import re
from math import radians, cos, sin, asin, sqrt


class CitiDistance():
    def __init__(self):
        pass

    def convert_to_radians(self,degree):
        return degree * math.pi / 180

    def distance(self,city1,city2):

        tmp_city1=city1.split(",")
        tmp_city2=city2.split(",")
        city1_lat=float(re.findall("\d+\.\d+",tmp_city1[0])[0])
        city1_lon=float(re.findall("\d+\.\d+",tmp_city1[1])[0])
        city2_lan=float(re.findall("\d+\.\d+",tmp_city2[0])[0])
        city2_lon=float(re.findall("\d+\.\d+",tmp_city2[1])[0])
        lon1 = radians(city1_lon)
        lon2 = radians(city2_lon)
        lat1 = radians(city1_lat)
        lat2 = radians(city2_lan)
        # Haversine formula
        dlon = lon2 - lon1
        dlat = lat2 - lat1
        a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2

        c = 2 * asin(sqrt(a))

        # Radius of earth in kilometers.
        r = 6371

        # calculate the result
        result = c * r
        result1=round(float(result), 3)
        print("Output: City 1 and City 2 are "+str(result1)+" km apart",)


c1 = CitiDistance()
city1=input("City 1: ")
city2=input("City 2: ")
c1.distance(city1,city2)
