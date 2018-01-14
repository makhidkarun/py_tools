
from ehex import ehex
import sys
sys.path.append("lib")

from character_tools import set_gender, set_name
from base_tools import roll_2d6

for x in range(1, 123):
  upp = ""
  
  for _ in range(6):
    upp = upp + str(ehex(roll_2d6()))

  gender  = set_gender()
  name    = set_name(gender)
  print("%d, %s, %s, %s" % (x, name, upp, gender))
