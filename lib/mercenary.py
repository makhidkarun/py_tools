import random
import sys
sys.path.append(".")
from character import Character

def get_career():
  return random.choice(['Army', 'Marines'])

def create_unit(size):
 
  if size == "fireteam": 
    create_fireteam()
  elif size == "squad":
    create_squad()
  elif size == "platoon":
    create_platoon()

def create_leader(rank):
  if rank == "CPL": 
    terms = 2
  elif rank == "SGT":
    terms = 3 
  elif rank == "GSGT":
    terms = 4
  elif rank == "LT":
    terms = 1
  elif rank == "CPT":
    terms = 2
  else:
    terms = 1

  ldr_data = {'terms': terms, 'career': get_career()}
  ldr = Character(ldr_data)
  print(rank + " " + ldr.display_string())

def create_platoon():
    print("Platoon Commander:  ")
    create_leader("LT")
    print("")
    print("Platoon Sergeant:  ")
    create_leader("GSGT")
    print("")

    print("First Squad")
    create_squad()
    print("Second Squad")
    create_squad()


def create_squad():
    create_leader("SGT")
    print("")
    print("== Fire Team Able:")
    create_fireteam()
    print("")
    print("== Fire Team Baker:")
    create_fireteam()
    print("")

def create_fireteam():
  create_leader("CPL")
  for s in range(3):
    pvt_data = {'terms':1, 'career': get_career()}
    pvt = Character(pvt_data)
    print("PVT " + pvt.display_string())
     
  
