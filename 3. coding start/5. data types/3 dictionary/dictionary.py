# dictionary is an unordered colloection of key-value pairs. In python dictionaries are defined within braces{} with each item being a pair in the form of key:value
# we get value using key 

# application: when we get data from data base mostly it is in the form of dictionary.

d= {
    "name":'mudasir',
    "age":18
}
print(d)            #return {'name': 'mudasir', 'age': 18}
print(d['name'])    #return 'mudasir'
print(type(d))      #return 'dict'

# dictionary is mutable we can update data
d['age']= 20
print(d)            #return {'name': 'mudasir', 'age': 20}