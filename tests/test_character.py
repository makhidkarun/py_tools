""" test_character.py """

import unittest
import sys
sys.path.append("lib")
import character

class TestCharacter(unittest.TestCase):
  def setUp(self):
    self.char = character.Character()
    self.char.generate()

  def test_terms(self):
    self.assertTrue( 1 <= self.char.terms <= 6)

  def test_gender(self):
    self.assertTrue(self.char.gender in ['M', 'F'])

if __name__ == '__main__':
  unittest.main()
