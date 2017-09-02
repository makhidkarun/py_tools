#!/usr/bin/env python
# relationships.py
# Track long term status.
# called by 
#   python relationships.py <person> <person> <starting roll> <modifier>

import random
import sys

def roll(modifier):
  return random.randint(1,6) + random.randint(1,6) + modifier

initial_months = [3, 2, 1]
person1 = sys.argv[1]
person2 = sys.argv[2]
start   = int(sys.argv[3])
mod     = int(sys.argv[4])
state   = (start - 8) / 2
months  = 0

status  = { -3: "Apart",
            -2: "Struggling",
            -1: "Cool",
             0: "Doing okay",
             1: "Really doing well",
             2: "Madly in love",
             3: "Married"
          }

while state > -3 and state < 3:
  this_month_roll = roll(mod)
  print("\t state %d" % state)
  print("\t this_month_roll %d" % this_month_roll)
  if months < len(initial_months):
    this_month_roll += initial_months[months]
  months += 1

  this_month_change = (this_month_roll - 8) / 2
  print("\t this_month_change %d" % this_month_change)
  state += int(this_month_change)
  state = min(3, state)
  state = max(-3, state)
  print("Month %d: %s and %s: %s" %(months, person1, person2, status[state]))
