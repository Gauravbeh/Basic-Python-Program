# there are two types of datatypes collective and fundamental datatypes.
# funcdamental dataypes() -> datatype is represent the which type of datatypes
# all fundamentals datatypes are mutable
'''int
   float
   complex
   string
   boolean
   '''
# int :- integer is represent the integer.
a = 10
print(a)

# float :- float is represent the floating pointings numbers.
b = 20.30
print(b)

# complex :- complex numbers represent complex number ex. c = 10 + 5j 
# c -> variable, 10 -> real number , 5j -> imagenery num

c = 10 + 5j
print(c)
print(type(c))

# string -> string is collection of charachter whithin a single code or doubl, tripple.

# str
name = "gaurav"
print(name)

# how to access char . from string

# Indexing -> indexing is a technique using help access the string. single charachter fetch. fetching the single element using indexing.
# -9 -8 -7 -6 -5 -4 -3 -2 -1 
# i  n  s  t  a  g  r  a  m
# 0  1  2  3  4  5  6  7  8
 
#syntax -> variable_name [index]
media = "instagram"
print(media[3])
print(media[-4])



# Slicing -> slicing is used to multiple characther accessing using slicing.

# syntax :- [start_index: end_index : stp_value]
# start index: slicing will start from start index
# end index : slicing stop before end index

# exercise
name = "rameshwaram"

#mesh
print(name[2:6:1])

# ram

print(name[0:3:1])

# shwara
print(name[4:-1:1])

#rws
print(name[-3:3:-2])
# war
print(name[-5:-2:1])

#ema
#print(name[])

cls = "the kiran academy"
print(cls[-7:17:1])
print(cls[-9:3:-1])
print(cls[-1:-8:-1])



# methods of str : methods return

# Upper() -> upper is a method because method call when using variable.
name = "my name is gaurav"
print(name.upper())

#lower() ->
name1 = "MY NAME IS GAURAV"
print(name.lower())

#title() -> first letter will be capital.
name2 = "the kiran academy"
print(name2.title())

# capatilize() -> capatilize only first letters.

name3 = "my name is gaurav. and paresh"
print(name3.capitalize())

# interview questions
'''what is str
WHAT IS indixing and slicing
what are the methods'''

# isalpha() => isalpha methods is used to specify the alfhabets and is alphabets present in methods return true. false
num1 = "raj"
print(name.isalpha())

num2 = "raj123"
print(name.isalpha())

num3 = "vaibhav patil"
print(num3.isalpha())

#isnumeric => isnumeric methods specify the numbers
num4 = "123"
print(num4.isnumeric())

#isalnum => isalnum is specify the both are number or string print true.
num5 = "vaibhav123"
print(num5.isalnum())

#isspace() 
num6 = " "
print(num6.isspace())

#istitle -> all first letters specify capital letters 
num7 = "vaibhav patil"
print(num7.istitle())
print(num7.isupper())

# sorted() function => sorted methods assend the assending order and sorted assending order
name4 = "rajesh"
print(sorted(name4))

# split () methods => Return a list of the substrings in the string, using sep as the separator string. single string converted into multiple seperated string
name5 = "gaurav patil pune"
print(name5.split())

# replace()
name6 = "the keeran academy"
print(name6.replace("ee","i"))
print(name6.replace("the keeran academy", "java by kiran academy"))
