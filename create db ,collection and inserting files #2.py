from pymongo import MongoClient                #creating DB
client = MongoClient()
myclient = MongoClient('localhost',27017)
mydbase = myclient["mongotest3"]
mycoll1=mydbase["records"]
mycoll2=mydbase["records2"]

#mylist = [
  #{ "id": 1, "name": "Aman", "address": "khi, pak"},
  #{ "id": 2, "name": "Faisal Hussain", "address": "khi, pak"},
  #{ "id": 3, "name": "Faisal Hafeez", "address": "khi, pak"},
  #{ "id": 4, "name": "Muhammad Hanif", "address": "khi, pak"},
  #{ "id": 5, "name": "Uzair", "address": "khi, pak"},
  #{ "id": 6, "name": "Saifullah", "address": "khi, pak"},
  #{ "id": 7, "name": "Faizan baig", "address": "khi, pak"},
  #{ "id": 8, "name": "Farheen", "address": "khi, pak"},
  #{ "id": 9, "name": "Tania", "address": "khi, pak"},
  #{ "id": 10, "name": "Kaneez Fatima", "address": "khi, pak"},
  #{ "id": 11, "name": "Siddiqa", "address": "khi, pak"},
  #{ "id": 12, "name": "Farwa Hussain", "address": "khi, pak"}  
#]

#x = mycoll.insert_many(mylist)
#record = {'_id': 4,"name": "Faisal","address": "Gulberg Karachi","country": ["Pakistan","Sweden","USA" {"state": "New york","California"}],"profile": "Experienced Web Developer"}
#record = {
  #'_id': 1,"name": "Faisal","address": "Gulberg Karachi","country": ["Pakistan","Sweden","USA"],"Profile": "Experienced Web Developer"
 # }
#x= mycoll2.insert_one(record)
#print(x.inserted_id)
#mongodb save function
#x = mycoll2.save({"_id": 2,"name": "Hina Faisal"})
#print(x)

#x = mycoll2.update_one({'name': 'Hina Faisal'},{$set: {'name': 'Ayesha Faisal'}})

#dblist = myclient.list_database_names()
#if input('Enter DB') in dblist:
    #print("The database exists.")
#else:
    #print("Not Present")

#print(dblist)
