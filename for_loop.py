# wap to print a name or percentage given dictionary.
student = {}
for i in range(3):
    name = input("Enter the name :")
    per = int(input("Enter the percentage :"))
    #student[i] = name
    student[name] = per
print(student)
