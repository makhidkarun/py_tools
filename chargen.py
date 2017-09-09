import getopt

import sys
sys.path.append("lib")
from character import Character

data = {}
if len(sys.argv) > 1:
  opts, args = getopt.getopt(sys.argv[1:], 'c:t:')
  for o, a in opts:
    if o == '-c':
      data['career'] = a
    elif o == '-t':
      data['terms'] = int(a)
      
char = Character()
char.generate(data)
char.display()
