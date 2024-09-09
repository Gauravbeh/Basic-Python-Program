#if elif else statment
#s1 = 42
#s2 = 41
#s3 = 40
'''s1 = int(input("Enter the s1 age :"))
s2 = int(input("Enter the s2 age :"))
s3 = int(input("Enter the s3 age :"))

if s1 > s2 and s2 > s3:
    print("s1 age is greater than s2 and s3")
elif s2 > s1 and s2 >  s3:
    print("s2 age is greater than s1,s3")
else:
    print("s3 is greater than s1,s2")
'''
#wap to check the nummber is positive or negative or zero

'''num = int(input("Enter the number :"))
if num > 0:
    print("Number is positive")
elif num < 0:
    print("Number is negative")
else:
    print("number is zero")'''

# grade user -per, 90 > a+, 80-90 a, 70-80 - b+ , 60-70 - b, 60 - c
marks = int(input("Enter the percentage :"))
if marks >= 90:
    print("A+ Grade")
elif marks >=80 and marks <= 90:
    print("A")
elif marks >= 70 and marks <= 80:
    print("B+")
elif marks>=60 and marks<=70:
    print("B")
else:
    print("c")

# calci
'''num1 = int(input("Enter the number 1"))
opr = (input("Enter the operator "))
num2 = int(input("Enter the num2"))

if opr == "+":
    print(num1+num2)
elif opr == "-":
    print(num1-num2)
elif opr == "*":
    print(num1*num2)
elif opr == "/":
    print(num1/num2)
else:
    print("Invalid operator")
print(type(opr))
'''

'''employee = {"uday":15000, "majnu":25000, "jay":35000, "veeru":37000, "pranav":78000, "kunal":60000, "vijay":45000}

# <2000 => 20%
# 20000 - 50000 => 10%
# 50000 => 5%
for name, sal in employee.items():
    if sal < 20000:
        employee[name] = (sal +(sal*20)/100)
    elif sal >= 20000 and sal <= 50000:
        employee[name] = (sal +(sal*10)/100)
    elif sal >=50000:
        employee[name] = (sal +(sal*5)/100)
    else:
        print("Invalid")
print(employee)
        
'''