""" worlds.py 
  python worlds.py [N]
"""

from __future__ import print_function

import argparse
import sys
sys.path.append("lib")
from world_tools import *

parser = argparse.ArgumentParser(description='Get number or worlds.')
parser.add_argument('number', metavar='N', type=int, nargs='?',
  help='Number of world names.', default=1)
args = parser.parse_args()

for i in range(args.number):
  print(world_name())
