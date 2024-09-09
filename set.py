# set datatype => set is a comma separated value within {}
# syntax => var_name = {val1,val2,...}

'''Defination => it is unordered, mutable, heterogenious, collection, 
immutable elements where insertion order is not preserved duplicate is not allowed '''

# unordered => index not present
# mutable => chengable we can add delete elements
# heterogenious => all type of data can be stored int, str, float.

# how to create set ?  => by using set () function.
# in set not update the value because set is unordered.

s1 = set([10,20])
print(s1)
s2 = set((10,20,30,20))
print(s2)

# discard
s1 = set={1,2,3,4}
s1.discard(3)
print(s1)

l2 = set(("guarav", "rohit"))
# l1.update("demo")
# print(l1)


# how to add data in set
# l1.add("rohit")
# print(l1)
# # delete data from set
# l1.pop()
# print(l1)