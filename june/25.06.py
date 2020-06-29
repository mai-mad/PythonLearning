# узнать сколько останется яблок в корзине если 3 человек разделят поровну 11 яблок
guys = 3
apples = 11 # 11 8 5 2
print(apples % guys)


# узнаь сколько достанется каждому ученику чокопаев если их 10 штук, а учеников 4

students = 4
chokopay = 16
print(chokopay // students) # ?4

# what is 2 in power 10
a = 2
b = 10
print(a ** b)


# shrinking

z = 8
z += 8
print(z) # 16

z -= 10
print(z)

z *= 10
print(z)

z += 2 # ?

# "=" VS "=="
x = 2
y = (x == 5)
if x <3:
    print(1)
else:
    print(2)
# 2
print(y)

# 2 example
z = 1
z == 2
z = 3
z == 4
if z==1:
    print(1)
if z==2:
    print(2)
if z==3:
    print(3)
if z==4:
    print(4)
# 4

x = 0
y = 1
z = 2

x == y
y == z
z = x

# x = 0
# y = 1
# z = 0

print(x, y, z)


# Task 3
x = 0
y == x
y = 1
z = y

# x - 0 y - 1 z - 1
print(x, y, z)


# Task
x = 0
y = 1
x = y
if x == y or y == x:
    print (1)
else:
    print(2)
# 2