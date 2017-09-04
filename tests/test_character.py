import unittest
import sys
sys.path.append("lib")
import character

class TestCharacter(unittest.TestCase):
  def setUp(self):
    self.char = character.Character()

  def test_upp_length(self):
    self.assertTrue(len(self.char.upp), 6)

  def test_terms(self):
    self.assertTrue( 1 <= self.char.terms <= 6)

  def test_show_upp(self):
    import string
    upp = self.char.show_upp(self.char.upp)
    self.assertTrue(all(c in string.hexdigits for c in upp))

  def test_gender(self):
    self.assertTrue(self.char.gender in ['M', 'F'])

if __name__ == '__main__':
  unittest.main()
