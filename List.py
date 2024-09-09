# 14-08-2024
# collective datatypes  => list, tuple, dict, set

# 1.list :- list comma sep. value in [] var=[v1,v2,..]
# list is ordered, mutable, herterogeneous collection of elements and duplicates elements are allowed.


'''num = [11,222,33,44,55,66]
print(num)
print(type(num))
num1 = ["gaurav", "puja", "rohit", "paresh"]
print(num1)'''

# mutable => list is mutable
'''l1 = [11, 22, 33, "gaurav"]
print("original value",l1)

l1[2] = "dada"
print(l1)'''

# herterogeneous
'''l2 = [11,22.22, "True",False]
print(l2)'''

# how to access data from list
'''by using indexing , slicing'''
'''l3 = [11,22,33,[44,55,66],77]
print(l3[-1]) 
print(l3[3][0])
print(l3[3][2])

l4 = ["rajesh","pavan",["arohi","prasad"], "shrushti"]
print(l4[2][0]) # arohi
print(l4[2][-1][0:3]) # pra
'''
# slicing
'''l5 = [11,22,33,44,55,66]
print(l5[-2:1:-1])

l6 = [11,22,33,[44,55,66,77,[1,2,3,4,5]],88]
# 11,22,33
print(l6[0:3:1])
#33,22
print(l6[2:0:-1])
#55,66,77
print(l6[3][1:4:1])
print(l6[4])

'''
# METHOD OF LIST : (all method print with variable) -> append, extend, sort, insert, remove, pop, index, count, revere, copy

# 1.append(value) :=>  Adds an item to the end of the list.

'''l7 = [11,22,33,44]
l7.append(55)
print(l7)

l8 =[11,22,[33,44],66]
l8[2].append(55)
print(l8)

# append method is used add element in last-> [1,2,3]
l9  = [11,22,[33,44,[1,2],55],66]
l9[2][2].append(3)
print(l9)   
'''
# 2.insert(index,value) :-=> insert method is used add a element in particular index number.(position)
# Inserts an  at element a specified position

''''l10 = [11,22,44,55,66]  # insert a value in 2 index
l10.insert(2,33)  
print(l10)
l10.insert(2,222)
print(l10)
l10.insert(3,444)
print(l10)

l11 = [11,22,[33,44,[1,2],55],66]
l11.insert(2,222)
print(l11)'''


# How to update data :-
# var_name[index] = updated_values
'''l12 =[11,22,33,44]
l12[2] = 333
print(l12)'''

'''l12[-1] = 555
print(l12)'''

'''l14 = [11,22,222,[33,44,[1,2],55],66]
#11 - 333
l14[0] = 333
'''

# how to delete data by using :=> 1.remove(), 2.pop(), 3.clear(), 4.del()

# 1.remove() => var.remove(value) ==> remove method used only removed first values ex 
# Removes the first occurrence of an element from the list.

'''ll1 = [11,22,222,[33,44,[1,2],55],66]
ll1.remove(222)
print(ll1)'''

'''ll1[2].remove(33)
print(ll1)
ll1[2][1].remove(1)
print(ll1)
'''
# 2.pop() => var.pop(index)  ==> 55 22 deleted values return pop method. 
# removes and returns the last elements form a python list by default.

'''stud = [11,22,33,[44,55,66,[2,3,4,2],55,7],999,22]
stud.remove(33)
stud.pop[]
print(stud)'''

# 3.clear() => var.clear() ==> all data list will be clear , Removes all elements from the list

'''stud1 = [1,2,3,4]
stud1.clear()
print(stud1)'''

# 4.count() => count how many times elements is present in the list.
'''ll2 = [1,2,3,1,1,4,5]
print(ll2.count(1))
'''
# 5.index() => index(item, [start, [end]]): Returns the index of the first occurrence of an element. 
# You can also specify a start and end index to search within.

'''ll3 = [1,2,3,4,5]
print(ll3.index(3))'''

# 6. reverse() => Reverses the elements of the list in place.

'''ll4 = [11,55,33,44]
ll4.reverse()
print(ll4)'''

#7.sort ()  :=> sort method is sort the list in assending order.
'''ll5 = [11,2,66,4,9]
ll5.sort()
print(ll5)'''

# 8.extend() :=> it is used to add all elements from one list to other list.
'''ll6 = [11,22]
ll7 = [1,2,3,4]
ll6.extend(ll7)
print(ll6)
'''
# 9.copy =>  Reverses the elements of the list in place.
# old_l1 = [1,2,3,4]
# new = old_l1.copy()
# print(new)

'''new_list = my_list.copy()'''

# Tuple => it is ordered, immutable, heterogeneous collection of ellements and duplicates are allowed.
# tuple is comma seperated. values within () paranthesis.
# var_name = (v1,v2,v3...)
# ordered -> ordered mens print the sequence throw
# immutable -> not changable
# heterogeneous -> all type data stored on tuple -> str, int, boolen, list
# homogenuous -> only one type of data stored on tuple.

# how to access elements from tuple by using indexig and slicing

# Difference between list And tuple
# tuple is used only not changable values.

'''from sys import getsizeof
ll8 = ["jay","dada"]
tp1 = ("jay","dada")
print(getsizeof(ll8))
print(getsizeof(tp1))
'''
# interview questions
'''What is tuple
   what are the methos of list
   what is diff bet list and tuple
   what is diff bet append and extend
   what is bet pop and remove'''

