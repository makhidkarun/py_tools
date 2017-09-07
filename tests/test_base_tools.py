""" test_base_tools """

import unittest
import sys
sys.path.append("lib")
import base_tools

class TestBaseTools(unittest.TestCase):
  
  def test_roll_1d6(self):
    rolls = []
    for r in range(1000):
      rolls.append(base_tools.roll_1d6())
    self.assertTrue(min(rolls) == 1)
    self.assertTrue(max(rolls) == 6)

  def test_roll_2d6(self):
    rolls = []
    for r in range(1000):
      rolls.append(base_tools.roll_2d6())
    self.assertTrue(min(rolls) == 2)
    self.assertTrue(max(rolls) == 12)

  def test_random_from_list(self):
    data_options = ['Marco', 'Irene', 'Tala', 'Ian', 
      'Akil', 'Alba', 'Hannah', 'Aldo']
    item = base_tools.random_from_list(data_options)
    self.assertTrue(item in data_options)
  
  def test_list_from_file(self):
    data_file = 'tests/data.txt'
    items = base_tools.list_from_file(data_file)
    self.assertTrue(len(items) == 8)


if __name__ == '__main__':
  unittest.main()
