x="hello"
y='world'

# Hello World! (final)

print(x.capitalize() + " " + y.capitalize() + "!")


x='HELLO'
y='world'

# hello WORLD

print(x.lower() + " " + y.upper())


# Hello World

print(x.capitalize() + " " + y.capitalize())


price = 15500
antisale = 3.5 # up
newprice1= price+(price*antisale/100)
print("after sale: " + str(newprice1))


# And Table
"""
x y AND (*)
0 0 0 
0 1 0 
1 0 0
1 1 1 

x y OR
0 0 0 
0 1 1
1 0 1 
1 1 1 

x NOT
0  1
1  0 

x = 3
if 0
    p(1)
else:
    p(2)
"""


# Lists (arrays)
thislist = ["apple", "banana", "cherry", "pear", "plum", "orange", "pomelo", "kiwi", "grape", "strawbery", "blueberry"]
print(thislist)

# apple pear
print(thislist[0], thislist[3])

#BANANA
print(thislist[1].upper())

print(thislist[-4])

print(thislist[0:2])

# cherry..grape
print(thislist[2:9])




