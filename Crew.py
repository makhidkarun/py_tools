import getopt

import sys
sys.path.append("lib")
from character import Character

data = {}
if len(sys.argv) > 1:
  opts, args = getopt.getopt(sys.argv[1:], 'm:s:')
  for o, a in opts:
    if o in ('-m', '--mercenary'):
      from mercenary import create_unit
      career_options = ['Army', 'Marines']
      size = a
      create_unit(size)
    elif o == '-s':
      print("ship crew not implemented yet.")
        
