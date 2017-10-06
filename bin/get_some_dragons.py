import pymongo

connection = pymongo.MongoClient('localhost', 27017)
db = connection.dragons
name = db.dragons
limit = 2

for  person in name.find({"skills.HeavyWpns" : {"$gt" : 0}}).limit(limit):
  #name_string = []
  #name_string.append(person['name'])
  #name_string.extend([ '[',  person['gender'], ']'])
  #name_string.extend(['Age:', str(person['age'])])
  #name_string.extend(['Morale:', str(person['morale']) ])
  #name_string.append(person['upp'])
  #string = ' '.join(name_string)
  #print(string)
  #for k,v in person['skills'].items():
  #  string += " " + k + '-' + str(v)
  #print
  
