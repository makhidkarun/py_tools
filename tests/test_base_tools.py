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
    data_file = 'tests/name_data.txt'
    items = base_tools.list_from_file(data_file)
    self.assertTrue(len(items) == 8)

  def test_multi_list_from_file(self):
    data_file = 'tests/spacer_skills2.txt'
    items = base_tools.multi_list_from_file(data_file)
    self.assertTrue(len(items) == 38)

  def test_modify_list(self):
    upp       = [ 7, 8, 9, 10, 11, 12]
    index     = 3
    modifier  = +1
    new_upp   = [ 7, 8, 9, 11, 11, 12]
    base_tools.modify_list(upp, index, modifier)
    self.assertTrue(new_upp == upp)

  def test_modify_list_empty_modifier(self):
    upp       = [ 7, 8, 9, 10, 11, 12]
    index     = 3
    new_upp   = [ 7, 8, 9, 11, 11, 12]
    base_tools.modify_list(upp, index)
    self.assertTrue(new_upp == upp)

  def test_validate_hex_int_max(self):
    num           = 23
    new_num       = base_tools.validate_hex_int(num)
    expected_num  = 15
    self.assertTrue(expected_num == new_num)

  def test_validate_hex_int_min(self):
    num           = -23
    new_num       = base_tools.validate_hex_int(num)
    expected_num  = 1
    self.assertTrue(expected_num == new_num)

if __name__ == '__main__':
  unittest.main()
