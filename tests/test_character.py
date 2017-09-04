import unittest
import sys
sys.path.append("lib")
import character

class TestCharacter(unittest.TestCase):
  def setup(self):
    self.char = character.Character()

  def test_upp_length(self):
    self.assertTrue(len(self.char.upp), 6)
    
  def test_display(self):
    self.char.display()
    
  ##  Oddly, by itself, this works.
  def test_setup(self):
    self.char = character.Character()
    self.char.display()
 
if __name__ == '__main__':
  unittest.main()
