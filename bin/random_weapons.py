#!/usr/bin/env python

import random
import sys

weapons = {}
weapon_options = ['missile', 'pulse_laser', 'sand', 'particle', 'beam_laser']

times = 1
if len(sys.argv) == 2:
  times = int(sys.argv[1])

for roll in range(times):
  wpn = random.choice(weapon_options)
  if wpn in weapons:
    weapons[wpn] += 1
  else:
    weapons[wpn] = 1

wpn_array = []
for wpn in weapons:
  wpn_array.append(wpn + ":" + str(weapons[wpn]))

wpn_array.sort()
print(', '.join(wpn_array))

