#!/usr/bin/python3.5
# -*- coding: utf_8 -*-

from json import load
from sys import argv
from math import pi


class Agent:
    """Classe qui représente une personne"""

    def __init__(self, position, attributes_from_dict):
        self.position = position

        for key, value in attributes_from_dict.items():
            self.__setattr__(key, value)

    def __str__(self):
        return str(self.__dict__)

    def __repr__(self):
        return str(self.__dict__)


class Position:
    """Classe qui représente une position"""

    def __init__(self, latitude_degrees, longitude_degrees):
        self.latitude_degrees = latitude_degrees
        self.longitude_degrees = longitude_degrees

    @property
    def latitude(self):
        """Latitude in radians"""
        return self.latitude_degrees * pi / 180

    @property
    def longitude(self):
        """Longitude in radians"""
        return self.longitude_degrees * pi / 180

    def __str__(self):
        return str(self.__dict__)

    def __repr__(self):
        return {'latitude': self.latitude, 'longitude': self.longitude}.__repr__()


class Zone:
    """Classe qui représente une zone"""

    ZONES = list()

    EARTH_RADIUS_KILOMETERS = 6371
    MIN_LONGITUDE_DEGREES = -180
    MAX_LONGITUDE_DEGREES = 180
    MIN_LATITUDE_DEGREES = -90
    MAX_LATITUDE_DEGREES = 90
    WIDTH_DEGREES = 1
    HEIGHT_DEGREES = 1

    def __init__(self, corner_bottom_left, corner_top_right):
        self.corner_bottom_left = corner_bottom_left
        self.corner_top_right = corner_top_right
        self.inhabitants = list()

    @classmethod
    def _create(cls):
        iter_latitudes = range(cls.MIN_LATITUDE_DEGREES, cls.MAX_LATITUDE_DEGREES, cls.HEIGHT_DEGREES)
        iter_longitude = range(cls.MIN_LONGITUDE_DEGREES, cls.MAX_LONGITUDE_DEGREES, cls.WIDTH_DEGREES)
        for latitude in iter_latitudes:
            for longitude in iter_longitude:
                corner_bottom_left = Position(longitude, latitude)
                corner_top_right = Position(longitude + cls.WIDTH_DEGREES, latitude + cls.HEIGHT_DEGREES)
                cls.ZONES.append(Zone(corner_bottom_left, corner_top_right))
        print(len(cls.ZONES))

    def contains(self, position):
        return min(self.corner_bottom_left.longitude, self.corner_top_right.longitude) <= position.longitude < \
               max(self.corner_bottom_left.longitude, self.corner_top_right.longitude) and \
               min(self.corner_bottom_left.latitude, self.corner_top_right.latitude) <= position.latitude < \
               max(self.corner_bottom_left.latitude, self.corner_top_right.latitude)

    @classmethod
    def find_zone_that_contains(cls, position):
        if not cls.ZONES:
            cls._create()
        longitude_index = int((position.longitude_degrees - cls.MIN_LONGITUDE_DEGREES) / cls.WIDTH_DEGREES)
        latitude_index = int((position.latitude_degrees - cls.MIN_LATITUDE_DEGREES) / cls.HEIGHT_DEGREES)
        longitude_bins = int((cls.MAX_LONGITUDE_DEGREES - cls.MIN_LONGITUDE_DEGREES) / cls.WIDTH_DEGREES)
        zone_index = latitude_index * longitude_bins + longitude_index
        zone = cls.ZONES[zone_index]
        return zone

    def add_inhabitant(self, inhabitant):
        self.inhabitants.append(inhabitant)

    @property
    def population(self):
        return len(self.inhabitants)

    @property
    def width(self):
        return abs(self.corner_bottom_left.longitude - self.corner_top_right.longitude) * self.EARTH_RADIUS_KILOMETERS

    @property
    def height(self):
        return abs(self.corner_bottom_left.latitude - self.corner_top_right.latitude) * self.EARTH_RADIUS_KILOMETERS

    @property
    def area(self):
        return self.height * self.width

    def population_density(self):
        return self.population / self.area

    def average_agreeableness(self):
        if not self.inhabitants or len(self.inhabitants) == 0:
            return 0
        return sum([inhabitant.agreableness for inhabitant in self.inhabitants]) / self.population


def populate(filename):
    with open(filename, 'r') as json_file:
        datas = load(json_file)
        for person in datas:
            position = Position(person.pop('latitude'), person.pop('longitude'))
            agent = Agent(position, person)
            zone = Zone.find_zone_that_contains(position)
            zone.add_inhabitant(agent)
            print('Population de la zone : {}'.format(zone.population))

if __name__ == '__main__':
    populate(argv[1])