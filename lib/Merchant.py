""" Merchant.py
  First run at a class to change a character.
"""
import random
import sys
sys.path.append("lib")
import character_tools

skill_list = ['Navigation', 'Pilot', 'Engineering', 'Computer']

class Merchant(object):
  def __init__(self, character, terms = 1):
    self.character = character
    self.terms     = terms
    self.character.age = character_tools.set_age(self.terms) 
    self.character.careers['Merchant'] = self.terms
    self.set_skills()
    
  def set_skills(self):
    for x in range(self.terms * 2): 
      new_skill = random.choice(skill_list)
      if new_skill in list(self.character.skills.keys()):
        self.character.skills[new_skill] += 1
      else:
        self.character.skills[new_skill] = 1 
