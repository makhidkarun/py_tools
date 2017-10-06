""" chargen.py """
# -*- coding: utf-8 -*-

import argparse

import sys
sys.path.append("lib")
from character import Character
from character_tools import *

parser = argparse.ArgumentParser(description='Create a character')
parser.add_argument('-t', '--terms', type=int, help='how many terms?', 
  default=roll_terms())
parser.add_argument('-c', '--career', help='what career?', 
  default=random_career())

args = parser.parse_args()
my_data = {}
my_data['name'] = "Veola Löfgren"
char = Character(my_data)
char.run_career(args.career, args.terms)
char.display()
