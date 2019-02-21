from pymongo import MongoClient
import pprint

#client = MongoClient()
client = MongoClient('mongodb://localhost:27017')
db = client['dbase1']
employeeslist = db.employees
#emp1 = {
    #'Name': 'Faisal',
    #'DOB': '31-MAY-1982',
    #'Address': 'Gulberg,Karachi, Pakistan'
#}
#insert details through array
#employeesarray = [{
    #'Name': 'Faisal',
    #'DOB': '31-MAY-1982',
    #'Address': 'Gulberg,Karachi, Pakistan'
#},{
    #'Name': 'Uzair',
    #'DOB': '31-MAY-1993',
    #'Address': 'Gulberg,Karachi, Pakistan'
#},{
    #'Name': 'Saifullah',
    #'DOB': '31-MAY-1995',
    #'Address': 'Gulberg,Karachi, Pakistan'
#},{
    #'Name': 'Faizan'    #'DOB': '31-MAY-1990',
    #'Address': 'Gulberg,Karachi, Pakistan'
#}

#]
#result = employeeslist.insert_many(employeesarray)
#for data in result.inserted_ids:
    #print("Added to Database " + str(result.inserted_ids))


#to find data 
finddata = employeeslist.find({
    'Name': 'Faisal'
})
for emp in finddata:
    print(emp)


#print(client)
