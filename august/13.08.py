import math

# print("shrimp")
#
# # while exam
#
# a = 3
# while a < 4:
#     a=a+1
# print("end.")
# #output: 3 end.
#
# a = 3
# while a < 4:
#     a=a+1
#     print(a)
# print("end.")
# #output: 4 end
#
# a = 3
# while a < 4:
#     print(a)
#     a=a+1
# print("end.")
# #output: 3 end

# last task
sum = 0
for x in range(0, 32, 2):
  sum = sum + x
print("end.")
print(sum)

# create a function with name Ura which print text: Ura =)
def ura():
  print("ura")
ura()

# create a function with name deff printing text: def

def deff():
  print("def")
deff()

# create a func with 1 number param printing the value of this param bigger by 1

def param(par):
  print (par + 1)
param(-1)

# create a func sum 2 numbers

def sum(value, value1):
  print(value + value1)
sum(10,1)

# create a func sum 3 numbers
def sum(value, value1, value3):
  print(value + value1 + value3)
sum(10,1,10)

#1 case
print(math.sqrt(2050))


#2case

a = math.sqrt(2050)
print (a)
print(a*2)


# this func returns sum of two numbers
def sum2(x, y):
  return x + y

# how to use sum2 function?
# case 1
a = sum2(2020, 1945)
print (a)

# case 2
print(sum2(2020,1945))
