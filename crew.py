""" crew.py
  python crew.py -m <'fireteam', 'squad', 'platoon'>
  python crew.py -s <int ship size>
"""
import argparse

import sys
sys.path.append("lib")
from character import Character

parser = argparse.ArgumentParser(description='Generate a ship or military crew')
group = parser.add_mutually_exclusive_group(required=True)
group.add_argument('-m', '--military', help='military unit of what size?')
group.add_argument('-s', '--ship', type=int, help='ship size?')

args = parser.parse_args()
if args.military is not None:
  from mercenary import create_unit
  create_unit(args.military)
elif args.ship is not None:
  from ship_crew import create_crew
  create_crew(args.ship)
else:
  print("Sorry. No capito.")
