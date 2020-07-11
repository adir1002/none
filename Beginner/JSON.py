import json
person={'first':'adir','last':'abu'}
person['City']= 'beer7'
person['HAB']= ['BB','FB','GOLF']
adir={}
adir['mo']=person
personj=json.dumps(adir)
x = '{ "name":"John", "age":30, "city":"New York", "list": ["aaa","bbb","ccc","ddd"], "zzz" : {"aaa":"ccc"}}'

# parse x:
y = json.loads(x)

# the result is a Python dictionary:
print(y["age"])
print(y["list"])
print(y["zzz"]["aaa"][1])

print(y)
print(personj)

print(personj[0])