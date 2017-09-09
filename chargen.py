""" chargen.py """

import getopt

import sys
sys.path.append("lib")
from character import Character

my_data = {}
if len(sys.argv) > 1:
  opts, args = getopt.getopt(sys.argv[1:], 'c:t:')
  for o, a in opts:
    if o == '-c':
      my_data['careers'] = a
    elif o == '-t':
      data['terms'] = int(a)
      
char = Character()
char.run_career(my_data)
char.display()

# Testing with an existing character.
new_data = { 'upp' : [7,8,9,9,8,7],
  'name'    : 'Ian Domici',
  'gender'  : 'M',
  'age'     : 24,
  'careers' : {'Firster': 3, 'Merchant': 3, 'Noble':2},
  'skills'  : {'Broker' : 2, 'GunCbt' : 1, 'Streetwise' :2}
  }

new_char = Character(new_data)
new_char.display()

limited_data = { 'gender' : 'F', 'name' : 'Rosa', 'age' : 18}
lim_char = Character(limited_data)
lim_char.run_career(limited_data)
lim_char.display()

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
