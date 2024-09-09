# for loop  => 

''' for var_name in iterable :
     body
     
     for loop print value element sequence lenth+
     for loop apply only iterable
     * for loop used to iteration
     * Interation => l = [1,2,3,4] => one one element fecth
     * iterable menas = > variable_name ex l
     
        l = [11,22,33,44,55] <-- iterable
        for num in l:
            print(num)
     '''
# for loop apply only string , tuples, list.
'''l = [11,22,33,44,55]
for num in l:
    print(num)
    print("Hello")
print("Welcome")


char = "kalyani"
for name in char:
    print(name)
'''
# write to iterate  all numbers from given list ?
l = [1,2,3,4,5,6,7,8,9,10]
for num in l:
    print(l)
# wap to iterate all char from given string ?
media = "instagram"
for name in media:
    print(name)

# wap to print square of all numbers from given list.
l2 = [1,2,3,4,5]
num1 = 0
for num in l2:
    num1 = num * num
    print(num1)

# write a program ==>list => name => print each name in uppercase
student = ["raj","puja","kalyani","arohi","divya"]
for name in student:
    print(name.upper())

# create a list of square of numbers from  given list and the print a new list.
l3 = [1,2,3,4,5]
l4 = []
for num in l3:
    l4.append(num*num)
print(l4)
#************************************************************************************************************************************************

# Range() ==> range is a datatype.

# range is a datatype it is used to generate a numners.
#var_name = range(sta_val,end_val,step_val)
# start_value => it will start from start value.
# end_value => it wiil stop before end value.
# step_value => by default + 1

'''  r=range(startValue, EndValue, StepValue) 
    for i in range(1,11,111)

'''
'''l5 = [1,2,3,4,5]

for i in range(1,6,2):
    print(i)
'''
# wap to print numbers form 5-1
'''for i in range(5,0,-1):
    print(i)
for i in range(1,6,1):
    print(i)'''

'''# frozenset
for i in range(1.2, 1.5, 0.1):
    print(i)'''
