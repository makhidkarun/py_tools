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


if __name__ == '__main__':
  unittest.main()
