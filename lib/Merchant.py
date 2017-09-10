""" Merchant.py
  First run at a class to change a character.
"""
import random

class Merchant(object):
  def __init__(self, character, terms = 1):
    self.character = character
    self.terms     = terms
    self.set_skills()

  def set_skills(self):
    skills = list(self.character.skills.keys())
    skill_list = ['Navigation', 'Pilot', 'Engineering', 'Computer']

    for x in range(self.terms * 2): 
      new_skill = random.choice(skill_list)
      if new_skill in skills:
        self.character.skills[new_skill] += 1
      else:
        self.character.skills[new_skill] = 1 
