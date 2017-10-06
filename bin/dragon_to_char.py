# -*- coding: utf-8 -*-
from pymongo import MongoClient
import random
import sys
sys.path.append("lib")
from character import Character
from character_tools import *

client = MongoClient()
db = client.dragons
dragon_list = db.dragons
dragon_count = dragon_list.count()

# This line pulls a random Dragon.
#one_dragon = dragon_list.find()[random.randrange(dragon_count)]
# This line pulls Veola Löfgren to test UTF-8.
one_dragon = dragon_list.find()[1141]
if sys.version_info[0] < 3:
  one_dragon['name'] = one_dragon['name'].encode("utf-8")
one_dragon['careers'] = {}
one_dragon['careers'][one_dragon['career']] = one_dragon['terms']
char = Character(one_dragon)
char.display()
