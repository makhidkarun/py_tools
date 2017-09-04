import random
import sys
sys.path.append("lib")
from character_tools import *

class Character(object):

  def __init__(self, my_data = None):
    if my_data == None:
      my_data = {}
    self.gender = my_data.get('gender', self.set_gender())
    self.name = my_data.get('name', self.make_name(self.gender))
    #self.upp  = my_data.get('upp', self.roll_upp())
    self.upp  = my_data.get('upp', roll_upp())
    self.terms  = my_data.get('terms', self.set_terms())
    self.age    = my_data.get('age', self.set_age(self.terms))
    self.career = my_data.get('career', self.set_career())
    self.skills = my_data.get('skills', self.set_skills(self.career, self.terms))

  def display(self):
    print("%-15s %s [%s] Age: %d " % 
      (self.name, self.show_upp(self.upp), self.gender, self.age))
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
    character_array = [self.name, self.show_upp(self.upp), self.gender, 
    self.age, self.career, self.terms]
    c_string = self.name + (" " * (20 - len(self.name)))
    c_string = c_string + self.show_upp(self.upp) + " "
    c_string = c_string + '[' + self.gender +']' + " Age: " + str(self.age)
    c_string = c_string + "\n  " + self.career 
    c_string = c_string + " (" + str(self.terms) + " terms)" 
    c_string = c_string + "\n  " + self.string_skills(self.skills)
    return c_string
  
  def make_name(self, gender):
    if gender == 'F':
      f_names = ['Vega', 'Gabbie', 'Giselle', 'Lanny', 'Ilana', 'Alba', 'Irene']
    else:
      f_names = ['Marco', 'Ian', 'Akil', 'Alan', 'Wilbur']
    f_name = random.choice(f_names)
    l_names = ['Domici', 'Stranger', 'Smith', 'Jones', 'Patterson']
    l_name = random.choice(l_names)
    return f_name + " " + l_name
    

  #def roll_upp(self):
  #  return [random.randint(1,6) + random.randint(1,6) for _ in range(6)]

  def set_age(self, terms):
    return 18 + (terms * 4) + random.randint(0,3)

  def set_career(self):
    return random.choice(['Army', 'Navy', 'Marines', 'Scouts',
      'Agent', 'Merchant', 'Citizen', 'Rogue'])

  def set_gender(self):
    return random.choice(['M', 'F'])

  def set_skills(self, career, terms):
    skills = {}
    if career in ['Army', 'Marines']:
      skill_list = ['GunCbt', 'VaccSuit', 'Leadership', 'Vehicle']
    elif career in ['Merchant', 'Navy', 'Scout']:
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
      
  
  def set_terms(self):
    """
    () -> int
    Returns a random integer between 1 and 6.

    >>> char = Character()
    >>> 0 < char.set_terms() <=6
    True
    >>> 6 < char.set_terms() 
    False
    """

    return random.randint(1,6)

  def show_upp(self, upp):
    return ''.join('%X' % u for u in upp)

if __name__ == '__main__':
  import doctest
  doctest.testmod()

