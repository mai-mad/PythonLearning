import random

def test():
    x = input("x: ")
    y = input("y: ")
    print(int(x) + int(y))


# function which sum two numbers
def test2(a,b):
    return a+b

# function which sum three numbers
def test3(a,b,c):
    return a+b+c

# function which multiply 4 own parameters
def test4(a,b,c,d):
    return a*b*c*d

def test5():
    name = input("Your name: ")
    print("WASSUP, "+ name + "!")

x = random.randint(0,10)
y = random.randint(0,10)
z = random.randint(0,10)
w = random.randint(0,10)

# print x and y
print(x, y, z, w)

# sum them via your own function
n = test2(x, y)
print(n)

# sum all three variables via test3 func
n = test3(x, y, z)
print(n)

n = test4(x, y, z, w)
print(n)

test5()