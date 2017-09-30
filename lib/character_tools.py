import random
import sys
sys.path.append("lib")
from base_tools import *

def roll_upp():
  return [roll_2d6() for _ in range(6)]

def set_gender():
  return random.choice(['M', 'F'])

def set_age(terms):
  return 18 + (terms * 4) + int((roll_1d6() / 2))

def add_career(terms=1):
  career  = random.choice(['Army', 'Navy', 'Marines', 'Scouts',
    'Agent', 'Merchant', 'Citizen', 'Rogue'])
  careers = { career : terms }
  return careers

def random_career():
  career  = random.choice(['Army', 'Navy', 'Marines', 'Scouts',
    'Agent', 'Merchant', 'Citizen', 'Rogue'])
  return career

def roll_terms():
  return roll_1d6()

def set_name(gender):
  import sqlite3
  f_name = ""
  l_name = ""
  if gender == 'F':
    try:
      conn    = sqlite3.connect('data/names.db')
      c       = conn.cursor()
      c.execute("SELECT * from humaniti_female_first ORDER BY RANDOM() LIMIT 1")
      f_name  = c.fetchone()[0]
      conn.close()
    except Exception:
      try:
        f_names = list_from_file('data/female_first_names.txt')
        f_name = random.choice(f_names)
      except IOError:
        f_name = "Glenda"
  else:
    try:
      conn    = sqlite3.connect('data/names.db')
      c       = conn.cursor()
      c.execute("SELECT * from humaniti_male_first ORDER BY RANDOM() LIMIT 1")
      f_name  = c.fetchone()[0]
      conn.close()
    except Exception:
      try:
        f_names = list_from_file('data/male_first_names.txt')
        f_name = random.choice(f_names)
      except IOError:
        f_name = 'George'
  try:
    conn    = sqlite3.connect('data/names.db')
    c       = conn.cursor()
    c.execute("SELECT * from humaniti_last ORDER BY RANDOM() LIMIT 1")
    l_name  = c.fetchone()[0]
    conn.close()
  except Exception:
    try:
      l_names = list_from_file('data/last_names.txt')
      l_name = random.choice(l_names)
    except IOError:
      l_name = 'Jones'
  return f_name + " " + l_name

def show_upp(upp):
  return ''.join('%X' % u for u in upp)

def set_skills(career, terms):
  skills = {}
  if career in ['Army', 'Marines']:
    try:
      skill_list = list_from_file('data/mercenary_skills.txt')
    except IOError:
      skill_list = ['GunCbt', 'VaccSuit', 'Leadership', 'Vehicle']
  elif career in ['Merchants', 'Navy', 'Scouts']:
    try:
      skill_list = list_from_file('data/spacer_skills.txt')
    except IOError:
      skill_list = ['Navigation', 'Pilot', 'Engineering', 'Computer']
  else:
    skill_list = ['Blade', 'GunCbt', 'Admin', 'Streetwise']

  for added_skill in range(terms * 2): 
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

def modify_upp(upp, mod):
  stats     = ['Str', 'Dex', 'End', 'Int', 'Edu', 'Soc']
  mod_array = mod.split()
  mod_value = int(mod_array[0])
  mod_stat  = mod_array[1]
  if mod_stat in stats:
    stat_index  = stats.index(mod_stat)
    upp[stat_index] += mod_value
  return upp 
  
def is_educated(upp):
  if upp[4] >= 8:
    return True
  return False 
