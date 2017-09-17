""" chargen.py """

from __future__ import print_function
""" Required to use print(rank, new_char) """

import getopt

import sys
sys.path.append("lib")
from world_tools import *

def usage():
    print('usage: worlds [-nh]')

if len(sys.argv) > 1:
    opts, args = getopt.getopt(sys.argv[1:], 'n:h')
    for o, a in opts:
        if o == '-n':
            if isinstance(a, str) and len(a) > 0:
                n = int(a)
                for i in range(n):
                    print(world_name())
        sys.exit()
    
    if o in ['-h', '--help']:
        usage()
        sys.exit()

print(world_name())