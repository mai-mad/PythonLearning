import random
# Write a function which says Привет Имя если возраст юзера до 7 лет иначе пишет Здарова!
def quest():
    name = input("Your name: ")
    print("WASSUP, " + name + "!")
    x = input("Your age: ")
    print("Your age is " + x)
    if int(x) < 7:
        print("YO!")
    else:
        print("HELLO!")

def foo(x, y):
    if x > 0 or y > 0:
        return 1
    elif x == 0 or y == 0:
        return 2
    else:
        return 3




#quest()

x = random.randint(-2,4)
y = random.randint(-2,4)

print("x: " + str(x))
print("y: " + str(y))

n = foo(-2, -2)
print(n)

name ="Mark" # just Mark is mistaken
print ("Hi " + name)

x = "5"
y = 10
print(int(x) + y) # fix error in this line!

a = 1
b = "2"
c = 3
d = "4"
print(a+int(b)+c+int(d)) # fix error in this line!


#this code is amazing
a = 1
b = 2
c = 3
print(a + int("0") + b + int("1") +c) # fix error in this line! #7


"""
x1 = 1
x2 = 2
x3 = 3
x4 = 4
x5 = 5
adf
asdf
asdf
asdf
asdf
asd
fas
df
asd
fas
fd
as
dfa
sdf
as
dfa
sdf
as
df
asd
fa
sdf
asd
f
"""