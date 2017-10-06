""" 
  character.py
  Character is a shell class 
    used for generating totally new characters,
    updating partially completed characters,
    or as a standard interface for existing characters.
"""
# -*- coding: utf-8 -*-

import random
import sys
sys.path.append("lib")
from character_tools import *

class Character(object):

  def __init__(self, my_data = None):
    self.create_framework()

    if my_data == None:
      self.generate_basic()
    else:
      for k,v in my_data.items():
        setattr(self, k, v)
      self.fill_out_char(my_data)
  
  def create_framework(self):
    self.name     = "".encode("utf-8")
    self.upp      = []
    self.age      = -1 
    self.gender   = ""
    self.careers  = {}
    self.skills   = {}
 
  def fill_out_char(self, my_data):
    self.gender   = my_data.get('gender', set_gender())
    self.upp      = my_data.get('upp', roll_upp())
    self.name     = my_data.get('name', set_name(self.gender))
    self.age      = my_data.get('age', 18)
    self.careers  = my_data.get('careers', {})
    self.skills   = my_data.get('skills', {})
 
  def generate_basic(self):
    self.gender   = set_gender()
    self.name     = set_name(self.gender)
    self.upp      = roll_upp()

  def run_career(self, career, terms = 0):
    """ Run a single career """
    self.career   = career
    if terms == 0:
      self.terms    = roll_terms()
    else:
      self.terms    = terms
    self.careers  = {self.career : self.terms}
    if self.age == -1:
      self.age      = set_age(self.terms)
    self.skills   = set_skills(self.career, self.terms)

  def display(self):
    if sys.version_info[0] < 3:
      name    = self.name.decode("utf-8")
    else:
      name    = self.name
    gender  = self.gender
    upp     = show_upp(self.upp)
    age     = self.age
    career_string = self.string_careers()
    skill_string  = self.string_skills()
    print("%-20s %-10s [%s] Age: %d\n  %s \n  %s" % 
      (name, upp, gender, age, career_string, skill_string))

  def string_careers(self):
    career_line   = ''
    career_keys   = list(self.careers.keys())
    career_keys.sort()
    for c in career_keys:
      career_line += c + " (" + str(self.careers[c]) + " terms) "
    return career_line
 
  def string_skills(self):
    skill_line = ''
    skill_keys = list(self.skills.keys())
    skill_keys.sort()
    for s in skill_keys:
      skill_line += s + '-' + str(self.skills[s]) + " "
    return skill_line
