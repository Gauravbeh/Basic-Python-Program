# if_else_statement

# check the student pass or fail
'''per = eval(input("Enter the percentage :"))
if per >= 40:
    print("Pass")
else:
    print("Fail")'''

#wap number is greater than or not

'''num = eval(input("Enter the Nummber :-"))
if num >= 18:
    print("Number is greater than 18")
else:
    print("Number is less than 18")'''

#wap to print list a positive numbers and list of negative numbers from given list.
'''l1=[]
l2=[]
l=[11,22,-33,44,-55,66,-77,88]
for num in l:
    if num >= 0:
       l1.append(num)
    else:
        l2.append(num)
print(l1)
print(l2)'''

#wap to print to check numbers is even or not
'''num = eval(input("Enerter the numbers :"))
if num % 2 == 0:
    print("Even",num)
else:
    print("Not",num)'''

#wap to check number is odd or even
'''num = eval(input("Enter the numbers:"))
if num % 2 == 0:
    print("Number is even:-", num)
else:
    print("Number is odd:-",num)'''

#wap to print list of even or set of odd numbers.
'''even=[]
odd = set()
number = [11,-22,33,44,55,66]

for i in number:
    if i % 2 ==0:
        even.append(i)
    else:
        odd.add(i)
print(even)
print(odd)'''

# wap to print a list of even num or list of odd num form given list.
'''even =[]
odd = []
l1 = [11,22,33,44,55,66]
for num in l1:
    if num % 2 ==0:
        even.append(num)
    else:
        odd.append(num)
print(even)
print(odd)'''

# wap to print of square of even num or cube of odd num from 1 to 10
'''for num in range(1,10):
    if num % 2 ==0:
        sq = num ** 2
        print("square of",num,"is",sq)  
    else:
        cub = num **3
        print("cube of",num,"is",cub)
'''
# print list of name of student => pass
# print list of name of student => pass

'''pa =[]
fai = []
result = {"kunal":67, "rajesh":98, "raj":34, "umesh":32, "lalit":65}

for ke, val in result.items():
    if val >= 40:
        pa.append(val)
        
    else:
        fai.append(ke)
print(fai)
print(pa)'''

'''result = {"kunal":67, "rajesh":98, "raj":34, "umesh":32, "lalit":65}
# > 40 => 2 increase
# < 40 => 10 increase
for name, per in result.items():
    if per >= 40:
        result[name] =per+2
    else:
        result[name] = per+10

print(result)'''

# delete => fail student data

'''result = {"kunal":67, "rajesh":98, "raj":34, "umesh":32, "lalit":65}
for per in list(result.keys()):
    if result[per]>= 40:
        print(result)
        result.pop(per)
print(result)
'''
'''result = {"kunal":67, "rajesh":98, "raj":34, "umesh":32, "lalit":65}

for i, j in result.items():
    if j <= 40:
    
     print(i,j)'''
'''result = {"kunal":67, "rajesh":98, "raj":34, "umesh":32, "lalit":65}
li=[]
li.append(result)
print(li)
for i in li.index("kunal"):
    #if i <= 40:
     print(i)
    '''

jay = 24
kuma = 21

jay = int(input("Enter the jay age :"))
kuma = int(input("Entter the kuma age :"))
if jay > kuma:
    print("jay age is greater than kuma")
else:
    print("kuma age is less than jay")