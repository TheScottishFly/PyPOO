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


def populate(filename):
    with open(filename, 'r') as json_file:
        datas = load(json_file)

        position = Position(datas[0].pop('latitude'), datas[0].pop('longitude'))
        first_agent = Agent(position, datas[0])
        print(first_agent)

if __name__ == '__main__':
    populate(argv[1])