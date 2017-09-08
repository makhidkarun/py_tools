import random

from .base_tools import *

def roll_upp():
  return [roll_2d6() for _ in range(6)]

def set_gender():
  return random.choice(['M', 'F'])

def set_age(terms):
  return 18 + (terms * 4) + int((roll_1d6() / 2))

def set_career():
  return random.choice(['Army', 'Navy', 'Marines', 'Scouts',
    'Agent', 'Merchant', 'Citizen', 'Rogue'])

def roll_terms():
  return roll_1d6()

def set_name(gender):
  if gender == 'F':
    try:
      f_names = list_from_file('data/female_first_names.txt')
    except:
      f_names = ['Frieda']
  else:
    try:
      f_names = list_from_file('data/male_first_names.txt')
    except:
      f_names = ['George']
  f_name = random.choice(f_names)
  try:
    l_names = list_from_file('data/last_names.txt')
  except:
    l_names = ['Jones']
  l_name = random.choice(l_names)
  return f_name + " " + l_name

def show_upp(upp):
  return ''.join('%X' % u for u in upp)

def set_skills(career, terms):
  skills = {}
  if career in ['Army', 'Marines']:
    skill_list = ['GunCbt', 'VaccSuit', 'Leadership', 'Vehicle']
  elif career in ['Merchants', 'Navy', 'Scouts']:
    skill_list = ['Navigation', 'Pilot', 'Engineering', 'Computer']
  else:
    skill_list = ['Blade', 'GunCbt', 'Admin', 'Streetwise']

  for add_skill in range(terms * 2): 
    new_skill = random.choice(skill_list)
    if new_skill in skills:
      skills[new_skill] += 1
    else:
      skills[new_skill] = 1 

  return skills
    
def add_skill(char, skill):
  if skill in char.skills:
    char.skills[skill] += 1
  else:
    char.skills[skill] = 1
 
