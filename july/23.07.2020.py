fruits = ["apple", "banana", "cherry", "pear", "persimmon", "date", "peach"]
i = 0
for x in fruits:
  #print (str(i)+" "+ x)
  i=i+1

# print all even positions:

i = 1
for x in fruits:
  #if i % 2  == 1:
    #print (str(i)+" "+ x)
  i=i+1

# print all odd positions:

i = 1
for x in fruits:
  #if i % 2  == 0:
    #print (str(i)+" "+ x)
  i=i+1

# print all fruits which starts with "p"
c = 'p'

#for x in fruits:
  #if x[0]==c:
    #print(x)

# print all fruits which starts with "r"
c = 'r'

#for x in fruits:
  #if x[3]==c:
    #print(x)

#5. print all fruits with third letter "a" or "e"
c = "a",
c1= "e"
'''for x in fruits:
  if x[2]==c or x[2]==c1:
    print(x)
'''

fruits.append("orange")
print(fruits)

#appends 3 items to fruits
# for i in range(3):
#   s = input("next fruit: ")
#   fruits.append(s)
# print(fruits)

fruits.insert(2, "blueberry")
print(fruits)
fruits.insert(6, "pomelo")
print(fruits)
fruits.remove("date")
print(fruits)
fruits.pop()
print(fruits)
fruits.pop()
print(fruits)
del fruits[5]
print(fruits)
del fruits[0]
print(fruits)
del fruits
print (fruits)