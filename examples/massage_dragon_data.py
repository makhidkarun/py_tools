# A very specific use case.
# Added here for edification. Or humor.
 
import collections
import pymongo
from pymongo import MongoClient
client = MongoClient()
db = client.dragons
dragon_list = db.dragons

# The infile is a subset. 
# The original had overlapping data.
infile = open('total_dragons.csv', 'r')

names   = []

for line in infile.readlines():
  line = line.strip()
  line_array = line.split(':')
  career  = line_array[0].strip()
  rank    = line_array[1].strip()
  title   = line_array[2].strip()
  name    = line_array[3].strip()
  if name not in names:
    names.append(name)
  else: 
    continue
  upp     = line_array[4].strip()
  gender  = line_array[5][0].strip()
  age     = line_array[6].strip()
  terms   = line_array[7].strip()
  morale  = line_array[8].strip()
  llp     = line_array[9].split()[0].strip()
  skills  = line_array[10].strip()
  skill_array = skills.split(',')
  skill_dict = {}
  for skill in skill_array:
    k = skill.split('-')[0]
    v = int(skill.split('-')[1])
    skill_dict[k] = v

  # Some people's Soc was artifically lowered.
  # This resets it. 
  if len(title) > 0:
    if title == 'Dame' or title == 'Knight':
      upp   = upp[:5] + 'B'
      soc_b_count += 1
    elif title == 'Baron' or title == 'Baroness':
      upp   = upp[:5] + 'C'
      soc_c_count += 1
    elif title == 'Marquis' or title == 'Marquesa':
      upp   = upp[:5] + 'D'
      soc_d_count += 1

  person = {
    "career"  : career,
    "rank"    : rank,
    "name"    : name,
    "upp"     : upp,
    "gender"  : gender,
    "age"     : int(age),
    "terms"   : int(terms),
    "morale"  : int(morale),
    "llp"     : llp,
    "skills"   : skill_dict 
  }
  db.dragons.insert_one(person)
