'''Dictionary => it is ordered, mutable, heterogeneous, collection of elements where the data is represent the form of keys and values'''
#Dictionary => keys,and values within {}.

'''dict
var = {k:v,,}
k => unique, immutable
v => duplicates, both
how to access data form dict
var[key]'''

'''last session
1.dict
2.how to create
3.how to access'''

# revision
# syntax : var = {k:v,..}
# student = {"name":"gaurav","age":23}
#key => unique, immmutable 
#values => duplicate, both muttable and immutable are accepted.

'''Studet1 = {"name":"raj", "age":21, "city":"shipur", "per":90}
print(Studet1)'''

# numbers1 = {"odd":[1,3,5,7,9], "even":(2,4,6,8,10)}
# numbers2 = {"odd"}


#Today session
# Realme mobile

'''realme ={"relame6":{"model":"6i","ram":"6gb","storage":"64gb","price":13000}, "realme6i":{"model":"7", "ram":"4gb", "storage":"48gb", "price":2500}}
print(realme)'''

# fav => moview
'''Pushpa = {"pushpa":{"hero":"aluarjun","released":"18-09-2002","Heroiene":"Rasmika"}}
print(Pushpa)

Genious = {"genious":{"hero":"utkarsh","released":"24-08-2028"}}
print(Genious)'''

# hero 3 film akshay kumar
'''akshaykumar = {"bhoolbuliya":{"released":"12-10-2007","actor":"vidya balan"},"khiladi":{"released":"12-04-1992","actress":"minakshi chaudhari"}}
print(akshaykumar)'''

# how to access data from dictionary
# by using key we can.. access the data
# Syntax => var[key]  => return value

'''student ={"name":"gaurav","age":22,"per":90}
print(student)
print(student["age"])
print(student["name"])'''

# one dictionary single student name age city perc , marks - four subjects

'''personal = {"name":"gaurav","age":22, "city":"shirpur", "percentage":100, "marks":{"python":45, "java":90, "c":87, "c++":55}}
print(personal)
print(personal["percentage"])
print(personal["marks"]["python"])
'''

# Interview Questions
'''what is dict
   how to access data from dict
   can we used duplicates key in dict?
   create dict to represent
'''

# Exercise => 2 brand => 3 model => details

# 21-08-2024 TODAY'S SESSION
'''CRUD
   UPDATE
   DELETE'''

# 1.how to access data from dict by using get method?

# get() => method 
# variable_name.method()
'''emp = {"name":"gaurav","salary":55000}

print(emp.get("name"))
print(emp.get("salary"))
'''

# 2.How to add data into dict?
# syntax :-> var[key] = value

'''student = {"name":"puja"}
student["city"] = "pune"
print(student)
student["salary"] = 55000
print(student)'''

# add method

'''oppoA15 = {"ram":"8gb", "storage":"126gb", "brand":"oppo"}
print(oppoA15["brand"])
print(oppoA15.get("brand"))
oppoA15["colour"] = "red"
print(oppoA15)'''

# how to access data and add colour
'''oppo = {"a14":{"ram":"12gb", "storage":"256gb"}, "a15":{"ram":"8gb","storage":"128gb"}}
print(oppo["a15"]["ram"])  # check the ram in a15 

oppo["a14"]["colour"] = "red"
print(oppo)
oppo["a15"]["colour"] = "pink"
print(oppo)'''

# how to delete data from dict? => pop(), update(), del
# by using pop method
'''student = {"name":"kalyani", "age":21, "city":"amalner"}
student.pop("age")
print(student)'''

# how to update data => name method already declared key on dictionary this key can be updated. this process called update method
#variable_name[key] = value
'''student = {"name":"kalyani", "age":21, "city":"amalner"}
student["salary"] = 3400 # add a value in dictionary
print(student)
student["name"] = "gaurav" # update the value on dictionary
print(student)'''

#bike
'''n150 ={"engine":"150cc", "power":"18.2ps", "mileage":"40kmpl"}
print(n150)'''

'''n150["mileage"] = "42kmpl" # update mileage 40 to 42kmpl
print(n150)'''

'''n150["colour"] = "black"  
print(n150)

n150.pop("colour")
print(n150)
'''
'''pulsar = {"n150":{"engine":"150cc", "power":"18.2ps", "mileage":"40kmpl"},"n160":{"engine":"160cc", "power":"18.2ps", "mileage":"50kmpl"},
           "n200":{"engine":"200cc", "power":"18.2ps", "mileage":"60kmpl"},}
print(pulsar)

print(pulsar["n160"]["power"]) # n160 power access

pulsar["n200"]["mileage"] = "33kmpl"  # n200 update the mileage 33kmpl
print(pulsar)

pulsar["n150"]["colour"] = "red"  # add colour in pulsar
print(pulsar)
pulsar["n160"]["colour"] = "pink"
print(pulsar)
pulsar["n200"]["colour"] = "black"
print(pulsar)

pulsar["n160"].pop("colour")
print(pulsar)

del pulsar["n2000"]["color"]
'''

# There are three methods of dictionary. => keys(), values(), items().
# 1.keys()  => it will reaturn list of all keys.
# syntax => var.keys()
'''student = {"name":"raj", "city":"pune", "per":89}
print(student.keys())


# 2.values() => it will reaturn list of all values
# synrax => var.values()
student = {"name":"raj", "city":"pune", "per":89}
print(student.values())

# 3.items() => it will return list of keys and values in tuple format

student = {"name":"raj", "city":"pune", "per":89}
print(student.items())
'''

# two ways to print values
# iteration return in dictionary -> return keys, list -> return elments, 
'''student ={"name":"gaurav","city":"pune", "per":90}
for i in student:
   print(student[i]) 
'''
# print a values only

'''student ={"name":"gaurav","city":"pune", "per":90}
for i in student.values():
    print(i)'''

# print value and keys by using items
student ={"name":"gaurav","city":"pune", "per":90}
for i in student.items():
    print(i)

'''SYMMARY todays 22-08-2024
dict
update
var[key] = value
delete
var.pop(key)
iteration
keys
values
items
keys
'''

# INTERVIEW QUESTIONS
'''
1.what is dict
2.how to update data?
3.how to delete data
4.how to iterate values from dict
5.what are the methods of dict'''

#task
# square = {1:1,2:4,3:9}
# for i in square.values():
#     print("print values",i)

# for i in square:
#     print(i)

# d = {1:{"name":"raj","city":"nagpur"},2:{"name":"rajesh","city":"nashik"}}
# print(d.keys())
# print(d.values())
# print(d[2].keys())

d1 = {222}
print(d1)



