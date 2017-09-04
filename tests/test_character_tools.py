""" test_character_tools """

import unittest
import sys
sys.path.append("lib")
from character_tools import *

class TestCharacterTools(unittest.TestCase):
  def setUp(self):
    self.upp = roll_upp()

  def test_upp_length(self):
    self.assertTrue(len(self.upp), 6)

  def test_show_upp(self):
    import string
    string_upp = show_upp(self.upp)
    self.assertTrue(all(str(c) in string.hexdigits for c in show_upp(self.upp)))

if __name__ == '__main__':
  unittest.main()
