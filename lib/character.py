import random

class Character(object):

  def __init__(self, my_data = None):
    if my_data == None:
      my_data = {}
    self.gender = my_data.get('gender', self.set_gender())
    self.name = my_data.get('name', self.make_name(self.gender))
    self.upp  = my_data.get('upp', self.roll_upp())
    self.terms  = my_data.get('terms', self.set_terms())
    self.age    = my_data.get('age', self.set_age(self.terms))
    self.career = my_data.get('career', self.set_career())

  def display(self):
    print("%-15s %s [%s] Age: %d " % 
      (self.name, self.show_upp(self.upp), self.gender, self.age))
    print("%-8s (%d terms)" % (self.career, self.terms))

  def make_name(self, gender):
    if gender == 'F':
      f_names = ['Vega', 'Gabbie', 'Giselle', 'Lanny', 'Ilana', 'Alba', 'Irene']
    else:
      f_names = ['Marco', 'Ian', 'Akil', 'Alan', 'Wilbur']
    f_name = random.choice(f_names)
    l_names = ['Domici', 'Stranger', 'Smith', 'Jones', 'Patterson']
    l_name = random.choice(l_names)
    return f_name + " " + l_name
    

  def roll_upp(self):
    return [random.randint(1,6) + random.randint(1,6) for _ in range(6)]

  def set_age(self, terms):
    return 18 + (terms * 4) + random.randint(0,3)

  def set_career(self):
    return random.choice(['Army', 'Navy', 'Marines', 'Scouts',
      'Agent', 'Merchant', 'Citizen', 'Rogue'])

  def set_gender(self):
    return random.choice(['M', 'F'])
  
  def set_terms(self):
    return random.randint(1,6)

  def show_upp(self, upp):
    return ''.join('%X' % u for u in upp)
