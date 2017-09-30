"""
  ship_crew.py
  Generates a minimal ship crew based on tonnage.
  python crew -s 400
"""

from __future__ import print_function
import random
import sys
sys.path.append(".")
from character import Character
import character_tools 

def get_career():
  return random.choice(['Scouts', 'Navy', 'Merchants'])

def create_crew(size):
  create_crewman("Pilot")
  create_crewman("Navg")
  create_crewman("Eng")
  for c in range(1, int(size/400)):
    create_crewman("Pilot")
    create_crewman("Navg")
  for c in range(1, int(size/300)):
    create_crewman("Eng")
  for c in range(1, int(size/100) + 1):
    create_crewman("Gunner")
 
def create_crewman(role):
  if role == "Eng": 
    skill = "Engineering"
  elif role == "Navg":
    skill = "Navigation" 
  elif role == "Helm":
    skill = "Pilot"
  elif role == "Gunner":
    skill = "Gunnery"
  else:
    skill = "Leader"

  crew = Character()
  crew.generate_basic()
  crew.run_career(get_career())
  character_tools.add_skill(crew, skill)

  print(role, crew)
  print("")
