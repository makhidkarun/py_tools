""" chargen.py """

from __future__ import print_function
""" Required to use print(rank, new_char) """

import getopt

import sys
sys.path.append("lib")
from character import Character
from character_tools import *

terms   = roll_terms()
career  = random_career()

my_data = {}
if len(sys.argv) > 1:
  opts, args = getopt.getopt(sys.argv[1:], 'c:t:')
  for o, a in opts:
    if o == '-c':
      career = a
    elif o == '-t':
      terms = int(a)
      
char = Character()
char.fill_out_char()
char.run_career(career, terms)
print(char)
print("")

# Testing with an existing character.
new_data = { 'upp' : [7,8,9,9,8,7],
  'name'    : 'Ian Domici',
  'gender'  : 'M',
  'age'     : 24,
  'careers' : {'Firster': 3, 'Merchant': 3, 'Noble':2},
  'skills'  : {'Broker' : 2, 'GunCbt' : 1, 'Streetwise' :2}
  }

new_char = Character(new_data)
rank = "Captain"
print(rank, new_char)
print("")

limited_data = { 'gender' : 'F', 'name' : 'Rosa', 'age' : 18}
lim_char = Character(limited_data)
lim_char.fill_out_char(limited_data)
lim_char.run_career(career='Firster', terms=1)
print(lim_char)
print("")
"""
### Sample output with the above.

Bart Courtois   776757 [M] Age: 33 
Army (3 terms) 
Admin-3 Blade-1 GunCbt-2 

Ian Domici      789987 [M] Age: 24 
Firster (3 terms) Merchant (3 terms) Noble (2 terms) 
Broker-2 GunCbt-1 Streetwise-2 

Rosa            78A978 [F] Age: 18 
Navy (0 terms) 
"""
