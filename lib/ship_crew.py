import random
import sys
sys.path.append(".")
from character import Character
import character_tools 

def get_career():
  return random.choice(['Scouts', 'Navy', 'Merchants'])

def create_crew(size):
  for c in range(int(size/400)):
    create_crewman("Pilot")
    create_crewman("Navg")
  for c in range(int(size/300)):
    create_crewman("Eng")
 
def create_crewman(role):
  if role == "Eng": 
    skill = "Engineering"
  elif role == "Navg":
    skill = "Navgigation" 
  elif role == "Helm":
    skill = "Pilot"
  else:
    skill = "Computer"

  crew_data = {'career': get_career()}
  crew = Character()
  crew.generate(crew_data)
  character_tools.add_skill(crew, skill)

  print(role + " " + crew.display_string())
  print("")

