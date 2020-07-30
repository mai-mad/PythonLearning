iprices = [0, 0, 0, 4990, 5990, 7990, 9990, 19990, 29990, 0, 45990, 53990, 999888, 123]

# print(len(iprices))

# for i in range(10):
#     print(i, " ")

for i in range(len(iprices)):
    iprices[i] = iprices[i] + iprices[i]*0.105

print(iprices)


# x = x + 1
# x += 1
# не перезаписывая массив вывести 1 процент от каждой цены
for i in range(len(iprices)):
    print(iprices[i]*0.01)

# перезаписывая массив вывести 1 процент от каждой цены (как будто бы сделали 99 процентов скидку)
for i in range(len(iprices)):
    iprices[i] = iprices[i] - iprices[i] * 0.99
print(iprices)


fruits = ["apple", "banana", "cherry", "orange"]
fruit = "orange"
if fruit in fruits:
  print("Yes, "+ fruit +" is in the fruits list")
else:
    print(fruit+" does not exist")