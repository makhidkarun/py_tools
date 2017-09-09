""" 
  Character, a shell class 
  It is used for generating totally new characters,
  updating partially completed characters,
  or as a standard interface for existing characters.
"""

import random
import sys
sys.path.append("lib")
from character_tools import *

class Character(object):

  def __init__(self, my_data = None):
    if my_data == None:
      self.generate_basic()
    else:
      for k,v in my_data.items():
        setattr(self, k, v)
      self.fill_out_char(my_data)
   
  def fill_out_char(self, my_data):
    self.gender   = my_data.get('gender', set_gender())
    self.upp      = my_data.get('upp', roll_upp())
    self.name     = my_data.get('name', set_name(self.gender))
    self.age      = my_data.get('age', 18)
 
  def generate_basic(self):
    self.gender   = set_gender()
    self.name     = set_name(self.gender)
    self.upp      = roll_upp()

  def run_career(self, my_data):
    if 'age' in my_data:
      self.terms  = int((my_data['age'] - 18) / 4)
    else:
      self.terms    = my_data.get('terms', roll_terms())
      self.age      = set_age(self.terms)
    self.careers  = my_data.get('careers', add_career(self.terms))
    self.skills   = set_skills(self.careers.keys(), self.terms)

  def display(self):
    print("%-15s %s [%s] Age: %d " % 
      (self.name, show_upp(self.upp), self.gender, self.age))
    career_line = self.string_careers(self.careers)
    print(career_line)
    skill_line = self.string_skills(self.skills)
    print(skill_line)
    print("")
  
  def string_careers(self, careers):
    career_keys   = list(careers.keys())
    career_keys.sort()
    career_line   = ''
    for c in career_keys:
      career_line = career_line + c + " (" + str(self.careers[c]) + " terms) "
    return career_line
 
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
    c_string = c_string + "\n  " + self.string_careers(self.careers)
    c_string = c_string + "\n  " + self.string_skills(self.skills)
    return c_string
