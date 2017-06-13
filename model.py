#!/usr/bin/python3.5
# -*- coding: utf_8 -*-

from json import load
from sys import argv


class Agent:
    """Classe qui représente une personne"""

    def __init__(self, position, attributes_from_dict):
        self.position = position

        for key, value in attributes_from_dict.items():
            self.__setattr__(key, value)

    def __str__(self):
        return str(self.__dict__)


class Position:
    """Classe qui représente une zone"""

    def __init__(self, latitude, longitude):
        self.latitude = latitude
        self.longitude = longitude

    def __str__(self):
        return str(self.__dict__)


def populate(filename):
    with open(filename, 'r') as json_file:
        datas = load(json_file)

        position = Position(datas[0].pop('latitude'), datas[0].pop('longitude'))
        first_agent = Agent(position, datas[0])
        print(position)
        print(first_agent)

if __name__ == '__main__':
    populate(argv[1])