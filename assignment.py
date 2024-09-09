# assignment operator :=> 
# +=
#n = 100
'''n+=1
print(n)'''

# *=
'''n*=2
print(n)
'''
# -=
'''n-=50
print(n)'''

# /=
'''n/=2
print(n)
'''
# wap to create a dictionary of square of numbers from given tuple 
'''t =(1,2,3,4,5)
d = {}

for i in t:
    d[i] = i **2
print(d)

# wap to create a dictionary of cube of nummbers from 11-20
d1 = {}
for i in range(11,21,1):
    d1[i] = i**3
print(d1)'''

# wap to print all marks value percentage
sum = 0
bushan_resutl = {"mar":30, "eng":40, "hindi":50, "math":60, "sci":70}
for i in bushan_resutl.values():
    sum =  sum + i
    #per = sum / 5
    per = sum /(100*len(bushan_resutl)) * 100
    
print(per)



