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

    MIN_LONGITUDE_DEGREES = -180
    MAX_LONGITUDE_DEGREES = 180
    MIN_LATITUDE_DEGREES = -90
    MAX_LATITUDE_DEGREES = 90
    WIDTH_DEGREES = 1
    HEIGHT_DEGREES = 1

    def __init__(self, corner_bottom_left, corner_top_right):
        self.corner_bottom_left = corner_bottom_left
        self.corner_top_right = corner_top_right
        self.population = 0

    @classmethod
    def create(cls):
        iter_latitudes = range(cls.MIN_LATITUDE_DEGREES, cls.MAX_LATITUDE_DEGREES, cls.HEIGHT_DEGREES)
        iter_longitude = range(cls.MIN_LONGITUDE_DEGREES, cls.MAX_LONGITUDE_DEGREES, cls.WIDTH_DEGREES)
        for latitude in iter_latitudes:
            for longitude in iter_longitude:
                corner_bottom_left = Position(longitude, latitude)
                corner_top_right = Position(longitude + cls.WIDTH_DEGREES, latitude + cls.HEIGHT_DEGREES)
                cls.ZONES.append(Zone(corner_bottom_left, corner_top_right))
        print(len(cls.ZONES))


def populate(filename):
    with open(filename, 'r') as json_file:
        datas = load(json_file)

        position = Position(datas[0].pop('latitude'), datas[0].pop('longitude'))
        first_agent = Agent(position, datas[0])
        print(first_agent)

if __name__ == '__main__':
    populate(argv[1])
    Zone.create()