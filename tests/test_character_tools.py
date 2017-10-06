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

  def test_show_upp_list(self):
    import string
    upp = [ 3, 4, 5, 10, 11, 12]
    string_upp = show_upp(upp)
    self.assertTrue(all(str(c) in string.hexdigits for c in show_upp(self.upp)))

  def test_show_upp_str(self):
    upp = "345ABC"
    self.assertTrue(upp == show_upp(upp))

  def test_show_upp_dict(self):
    upp = { "Str" : 3, "Dex" : 4, "End" : 5, "Int" : 10, "Edu" : 11, "Soc" : 12}
    new_upp = show_upp(upp)
    self.assertTrue(new_upp == "345ABC")

  def test_is_uneducated(self):
    upp =   [7,7,7,7,7,7]
    self.assertFalse(is_educated(upp))
   
  def test_is_educated(self):
    upp =   [7,7,7,7,8,7]
    self.assertTrue(is_educated(upp))
   
  def test_modify_upp_raise(self):
    upp =   [7,7,7,7,7,7]
    new_upp = modify_upp(upp, '+2 Int')
    expected_upp = [7,7,7,9,7,7]  
    self.assertTrue(new_upp == expected_upp)

  def test_modify_upp_lower(self):
    upp =   [7,7,7,7,7,7]
    new_upp = modify_upp(upp, '-2 End')
    expected_upp = [7,7,5,7,7,7]  
    self.assertTrue(new_upp == expected_upp)

  def test_modify_upp_over_max(self):
    upp =   [7,7,7,7,7,7]
    new_upp = modify_upp(upp, '+10 Int')
    expected_upp = [7,7,7,17,7,7]  
    self.assertTrue(new_upp == expected_upp)

  def test_modify_upp_invalid(self):
    upp =   [7,7,7,7,7,7]
    new_upp = modify_upp(upp, '-2 Bork')
    expected_upp = [7,7,7,7,7,7]  
    self.assertTrue(new_upp == expected_upp)

if __name__ == '__main__':
  unittest.main()
