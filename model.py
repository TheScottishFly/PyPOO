#!/usr/bin/python3.5
# -*- coding: utf_8 -*-

from json import load
from sys import argv


class Agent:

    def __init__(self, attributes_from_dict):
        for key, value in attributes_from_dict.items():
            self.__setattr__(key, value)


def populate(filename):
    with open(filename, 'r') as json_file:
        datas = load(json_file)

        first_agent = Agent(datas[0])
        print(first_agent.conscientiousness)

if __name__ == '__main__':
    populate(argv[1])