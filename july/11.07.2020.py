fruits = ["apple", "banana", "cherry", "pear", "persimmon", "date", "peach"]

i = 1
for x in fruits:
  print (str(i)+" "+ x)
  i=i+1


# print all even positions:

i = 1
for x in fruits:
  if i % 2  == 0:
    print (str(i)+" "+ x)
  i=i+1

# print all odd positions:

i = 1
for x in fruits:
  if i % 2  == 1:
    print (str(i)+" "+ x)
  i=i+1

# print all fruits which starts with "p"
c = 'p'

for x in fruits:
  if x[0]==c:
    print(x)

# print all fruits which second letter "a"
c = "a"
for x in fruits:
  if x[1]==c:
    print(x)

#2 print all fruits with third letter "a"
c = "a"
for x in fruits:
  if x[2]==c:
    print(x)

#print all fruits with last letter "e"
c = "e"
for x in fruits:
  if x[3]==c:
    print(x)
#5. print all fruits with first letter "a" or "b"
c = "a",
c1= "b"
for x in fruits:
  if x[0]==c or x[0]==c1:
    print(x)
