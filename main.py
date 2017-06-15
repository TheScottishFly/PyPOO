#!/usr/bin/python3.5
# -*- coding: utf_8 -*-

from json import load
import sys
from argparse import ArgumentParser
import logging
from os import path

from graph import *
from model import *


def populate(filename):
    with open(filename, 'r') as json_file:
        datas = load(json_file)
        for person in datas:
            position = Position(person.pop('latitude'), person.pop('longitude'))
            agent = Agent(position, person)
            zone = Zone.find_zone_that_contains(position)
            zone.add_inhabitant(agent)
    agreeableness_graph = AgreeablenessGraph()
    agreeableness_graph.show(Zone.ZONES)


def parsing():
    parser = ArgumentParser(description='PyPOO, visualization program of population datas')
    parser.add_argument('file', metavar='F', type=str, nargs='?', action='store',
                        help="Must be a JSON file, he contains inhabitants datas")
    parser.add_argument('-v', '--verbose', dest="verbose", action="store_true", default=False, help="Increases logging")
    return parser.parse_args()


if __name__ == '__main__':
    args = parsing()
    if not args.file or path.splitext(args.file)[1] != '.json' or not path.exists(args.file):
        print("JSON file required !")
        sys.exit(1)
    if args.verbose:
        logging.basicConfig(format="[%(asctime)s] %(message)s", datefmt="%d-%m-%Y %H:%M:%S", level=logging.DEBUG)
    else:
        logging.basicConfig(format="[%(asctime)s] %(message)s", datefmt="%d-%m-%Y %H:%M:%S", level=logging.INFO)
    populate(args.file)