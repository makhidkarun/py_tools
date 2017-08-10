#!/usr/bin/env python

# Gives sum of two non-cryptographically secure ints between 1 and 6.

# If called with a number gives that many results.
#   roll_dice.py 4
#   8
#   9
#   8
#   3

import random
import sys

random.seed()

times = 1
if len(sys.argv) == 2:
  times = int(sys.argv[1])

for i in range(times):
  print random.randint(1,6) + random.randint(1,6)
