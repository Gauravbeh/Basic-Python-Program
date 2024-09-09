# if_statement :=> group of statement

'''if statement is used to one condition check at a time when the if statement is used.
    check one condition at a time'''

'''age = int(input("Enter the age : "))
if age > 18:
    print("You are eligible for voting")
'''

'''l = [11,-22,33,-44,55,-66]
# iterate only negative numbers

for num in l:
    if num < 0:
          print(num)'''

# wap to check numbers is even
'''num = int(input("Enter the number :"))
if num %2 == 0:
    print("Number is even")'''

# wap to check number is odd
'''num1 = int(input("Enter the number"))
if num1 %2 == 1: 
   
    print("Number is odd")'''

# wap  to print even numbers
'''l = [11,22,33,44,55]
for num in l:
    if num%2 == 0:
        print("number is even",num)'''

# wap to print list of squar of odd numbers from given list
'''l = [1,2,3,4,5,6]
sq = []
for num in l:
    if num%2 == 1:
      sq = num**2  
      sq.append(sq)
print(sq)'''

#wap to print a set of cube of even numbers form given list.
'''l1 = [1,2,3,4,5,6]
s1 = set()
for num in l1:
    if num%2 == 0:
        cub = num**3
        s1.add(cub)
print(s1)
'''
# print a list => pass => name , condition is => 40 above
'''result = {"amruta":78, "bharti":35, "dipak":31, "harshda":67}
p =[]
for num in result:
    if result[num] >= 40:
        p.append(num)    
print(p)'''

'''result = {"amruta":78, "bharti":35, "dipak":31, "harshda":67}
p =[]
for num, per in result.items():
    if per >= 40:
        p.append(num)
print(p)'''

# p = {"aja":25, "yash":66, "rohit":8}
# dict => eligible => voting add new dictionary

'''d = {"ajay":25, "vijay":45, "sujay":12, "pranav":1}
em ={}
for name , age in d.items():
    if age >= 18:
        em[name] = age
print(em)'''

#Exercise => 23-08-2024
#1.what are flow control statement in python?
'''There are three flow control statement
   1.Conditional Statement
   2.Iterative statement
   3.Transfer statement'''

#2.what are Conditional statement in python?
'''There are three types of conditional statements
   1.If statement..
   2.If else statement
   3.if elif else statement'''

#3.Explain if statement with example
'''num = int(input("Enter the Number:"))
if num >= 0:
    print("Number is positive ")'''

'''Explain -> if statement is a type of condition statement, 
to check the given condition it true or false. it will return bool values'''

#4.dict => square => even numbers
num = [1,2,3,4,5,6]
d1 ={}
for i in num:
    if i%2 == 0:
        sq = i ** 2
        d1[i] = sq
print(d1)

