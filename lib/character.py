""" Charater.py, a shell class """

import random
import sys
sys.path.append("lib")
from character_tools import *

class Character(object):

  def generate(self, my_data = None):
    if my_data == None:
      my_data = {}
    self.gender = my_data.get('gender', set_gender())
    self.name = my_data.get('name', set_name(self.gender))
    self.upp  = my_data.get('upp', roll_upp())
    self.terms  = my_data.get('terms', roll_terms())
    self.age    = my_data.get('age', set_age(self.terms))
    self.career = my_data.get('career', set_career())
    self.skills = my_data.get('skills', set_skills(self.career, self.terms))

  def display(self):
    print("%-15s %s [%s] Age: %d " % 
      (self.name, show_upp(self.upp), self.gender, self.age))
    print("%-8s (%d terms)" % (self.career, self.terms))
    skill_line = self.string_skills(self.skills)
    print(skill_line)
    print("")

  def string_skills(self, skills):
    skill_keys = list(skills.keys())
    skill_keys.sort()
    skill_line = ''
    for s in skill_keys:
      skill_line = skill_line + s + '-' + str(self.skills[s]) + " "
    return skill_line

  def display_string(self):
    c_string = self.name + (" " * (20 - len(self.name)))
    c_string = c_string + show_upp(self.upp) + " "
    c_string = c_string + '[' + self.gender +']' + " Age: " + str(self.age)
    c_string = c_string + "\n  " + self.career 
    c_string = c_string + " (" + str(self.terms) + " terms)" 
    c_string = c_string + "\n  " + self.string_skills(self.skills)
    return c_string
  
if __name__ == '__main__':
  import doctest
  doctest.testmod()
