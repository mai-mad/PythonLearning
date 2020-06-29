import random

# 1. Создать функцию которая генерирует 10 чисел от 0 до 10 и выводит их.
def test():
    for i in range(0, 10):
        n = random.randint(1, 10)
        print(str(i + 1) + ". n = " + str(n))

# 2. Создать функцию которая принимает 3 параметра и выводит максимальное из них.
def test2(a, b, c):
   if a > b and a > c:
       return a
   elif b > a and b > c:
       return b
   elif c > a and c > b:
       return c

#test()

'''
print(test2(4, 40, 30))
print(test2(4, 30, 60))
print(test2(70, 15, 40))
'''

_ = 2
__ = 3
___=4
my_age = 150

#vars with correct names

my_name = 1
_ = 3

#vars with incorrect names
'''
- = 2
. = 3 
^!%^ = 2
*^_=3
'''
#print(_+__+___+my_age) # 2+3+4 = 9


'''
aaa = 2+
. = 3 -
a2a = 3 +
a22 = 5 +
2a2 = 3 -
_a  = 5 +
a_  = 6 +
a 2 = 7 -
a-a = 8 -
'''

age = 8
aGe = 10
AGE = 12
Age = 13
agE = 14
AgE = 15
AGe = 16
aGE = 17
print (age+aGe+AGE)

x, y, z, w= "Orange", "Banana", "Cherry", "Apple"
print(x)
print(y)
print(z)
print(w)

