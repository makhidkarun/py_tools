import sys
sys.path.append("lib")
from character import Character

x_dict = {'career' : 'Navy'}
x = Character(x_dict)
x.display()
print('')

y_dict = {'career' : 'Merchant'}
y = Character(y_dict)
y.display()
print('')

z = Character()
z.display()
print('')
