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

def modify_attribute(data):
  """
  NOTE:  This is untested!!!
  Takes a dict of an instance, an attribute to modify, a key in that 
  attribute, and an optional value.
  Creates the key,value pair with a default if key does not exist.
  """
  inst      = data,get('instance')
  attribute = data.get('attribute')
  key       = data.get('key', None)
  value     = data.get('value', 1) 
 
def list_from_file(file):
  """
  Takes a file of one list item per line. 
  Returns a list of those items.
  Removes whitespace and blank lines.
  """
  datafile = open(file, 'r')
  items = []
  for line in datafile:
    line  = line.strip()
    if line.startswith("#"):
      continue
    if len(line) > 0:
      items.append(line)
  return items

def multi_list_from_file(file):
  """
  Takes a file of one set of items per line.
  The first item must be an Int > 0.
  The rest of the line will be appended to the list as a string.
  Returns that list.
  """
  datafile  = open(file, 'r')
  items   = []
  for line in datafile:
    line  = line.strip()
    if line.startswith('#') or len(line) < 3:
      continue
    else:
      line_array  = line.split()
      count       = int(line_array[0])
      rest        = ' '.join(line_array[1:])
      for _ in range(count):
        items.append(rest)
  return items


def random_from_list(l):
  """
  Returns a random item from the list.
  """
  return random.choice(l)

def modify_list(l, index, modifier = 1):
  """
  Modifies existing list with the modified value at index.
  """
  l[index] = l[index] + modifier
  
def validate_hex_int(num):
  """
  Returns an int between 1 and 15 inclusive.
  """
  num = min(15, num)
  num = max(1, num)
  return int(num)

if __name__ == '__main__':
  list_from_file('data.txt')

