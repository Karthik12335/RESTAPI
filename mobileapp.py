'''
insert data into database
                inser(POST)
mobileapp.py---------------->apiapp

'''

import json
import requests 


#Insert Data

'''
#d={'name':'Harry','rno':35,'per':89.9}
d={'name':'Rahul','rno':38,'per':80.9}
#d={'name':'Karthik','rno':36,'per':99.9}
js=json.dumps(d)
URL="http://localhost:8000/insert"

res=requests.post(url=URL,data=js)
data=res.json()
print(data)
'''


#Retrive data
'''
URL="http://localhost:8000/getall"

res=requests.get(url=URL)
data=res.json()
print(data)

'''

#Retriving a Single record
'''
d={'id':2}
jason_data=json.dumps(d)
URL="http://localhost:8000/getstudent"

res=requests.get(url=URL,data=jason_data)
data=res.json()
print(data)
'''

#Deleting a record 
'''
d={'id':1}
jason_data=json.dumps(d)
URL="http://localhost:8000/delete"

res=requests.delete(url=URL,data=jason_data)
data=res.json()
print(data)
'''

#updating the record

d={'id':3,'name':'Rakesh'}
js=json.dumps(d)
URL="http://localhost:8000/update"

res=requests.put(url=URL,data=js)
data=res.json()
print(data)