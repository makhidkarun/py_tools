""" base_tools for Cepheus Engine and other 2d6 SciFi games. """

import random

def roll_1d6():
  """ 
  Generates a non-cryptographically secure int on the bell curve 
  within the 1-6 range inclusive.
    () -> int
  """
  return random.randint(1,6)

def roll_2d6():
  """ 
  Generates a non-cryptographically secure int on the bell curve 
  within the 2-12 range inclusive.
    () -> int
  """
  return roll_1d6() + roll_1d6()
