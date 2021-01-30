"""
import json
a = {'name':'covid','age':1,"location":"china"}

b=json.dumps(a)
print(a)
print(b)
"""

"""
import json

with open("demo.json","r") as jsonfile:
    jsontxt=jsonfile.read()
#JSON String into a dictionary
dicttype=json.loads(jsontxt)
print(dicttype)
"""

"""
import json
my_dictionary = {
    "name":"Alexandaer Graham Bell",
    "job_title":"CEO",
    "company_name":"Bell System",
    "age":75,
    "emails":[{"email":"alex@bell.com","type":"work"}],
    "my_neighbor":False
}

#print(my_dictionary)

#unformatted_json=json.dumps(my_dictionary)
#print(unformatted_json)

formatted_json=json.dumps(my_dictionary,indent=4,sort_keys=True,separators=(",","="))
print(formatted_json)
unformatted_json=json.dumps(my_dictionary)
#convert JSON into a dictionary
dict1=json.loads(unformatted_json)
print(dict1)
print("Individual Key:job_title,value:",dict1["job_title"],end="\n")
"""

"""
#print all keys and their values
for key,value in dict1.items():
    print("key:",key,"value:",value)
"""
