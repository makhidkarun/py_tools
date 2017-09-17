"""
  world_tools.py
  Functions useful in world generation.
"""

import random
import sys
sys.path.append("lib")
from base_tools import *

#Loaded here globaly so it's done only once on import
world_name_list = list_from_file('data/world_names.txt')

def salt_name(name=''):
    # Add random 'salt' to the world name in the from of a prefix or suffix
    limit = 15 - len(name)
    d20 = random.randint(1, 20)
    
    if d20 <= 2:
        name = 'New ' + name
    elif 2 <= d20 <= limit:
        # Duplication in the list is deliberate to stack the odds
        suffix = random.choice([' Prime', ' Prime', ' Alpha', ' Alpha',
                                ' Beta', ' Gamma', ' Delta', ' Minor',
                                ' Majoris', ' II', ' II', ' III', ' III',
                                ' IV', ' IV', ' V', ' V', ' VI', ' IX'])
        name = name + suffix
    
    return name

def world_name(salt=True):
    if len(world_name_list) > 0:
        # We don't do random.choice() because we want to remove previously used names
        name_number = random.randint(0, (len(world_name_list) - 1))
        name = world_name_list.pop(name_number).rstrip()

        if salt and len(name) < 8:
            name = salt_name(name)

    return name
