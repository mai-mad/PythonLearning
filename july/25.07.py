#6. create list from numbers and sum them
numbers=[1,6,1000000,2,8,10,2000000,-1000000,5]      #1000017

# sum = 0
# for i in numbers:
#     sum = sum + i
# print(sum)

# mul = 1
# for i in numbers:
#     mul = mul * i
# print(mul)

# sum = 0
# for i in numbers:
#     if i < 1000000:
#         sum = sum + i
# print(sum)

#7. Concat all elements from the list to one string
# frase=["he ", "likes ", "timaty ", "!"]
# s = ""
# for i in frase:
#     s = s + i
# print(s)

#8. create list from numbers and print all even elements
# for i in numbers:
#     if i % 2 == 0:
#         print(i)


# for i in numbers:
#     if i % 2 == 1:
#         print(i)
# sum = 0
# # for i in numbers:
# #     if i % 2 == 0:
# #         sum = sum + i
# # print(sum)

fruits = ["apple", "banana", "cherry"]
# del fruits [1]
# # print(fruits)
# # fruits.insert(1, "cherry")
# # print(fruits)

# fruits.remove("banana")
# fruits.append("cherry")
# print(fruits)

#["apple", "banana", "cherry"] -> [banana, cherry, apple]


fruits.remove("apple", "banana", "cherry")
fruits.append("banana", "cherry", "apple")
print(fruits)