""" crew.py
  python crew.py -m <'fireteam', 'squad', 'platoon'>
  python crew.py -s <int ship size>
"""
import argparse

import sys
sys.path.append("lib")
from character import Character

parser = argparse.ArgumentParser(description='Generate a ship or military crew')
parser.add_argument('-m', '--military', help='military unit of what size?',
  default='fireteam')

args = parser.parse_args()
if 'military' in list(args.keys()):
  print(args.military)

sys.exit()

if len(sys.argv) > 1:
  opts, args = getopt.getopt(sys.argv[1:], 'm:s:')
  for o, a in opts:
    if o in ('-m', '--mercenary'):
      from mercenary import create_unit
      size = a
      create_unit(size)
    elif o == '-s':
      from ship_crew import create_crew
      create_crew(int(a))
        
