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
      size = a
      create_unit(size)
    elif o == '-s':
      from ship_crew import create_crew
      create_crew(int(a))
        
