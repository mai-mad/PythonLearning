fruits = ["apple", "banana", "cherry", "pear", "plum", "orange", "pomelo", "kiwi", "grape", "strawbery", "blueberry"]

vegetables = ["cucumber", "tomato", "potato"]

numbers = [1, 2, 3]

dates = [1945, 2020, 2003]

ages = [18, 1, 90, 58]

seasons = [1, 2, 3, 4] # +

powers = [1, 2, 4, 8, 16, 32]

weights = [58.5, 75.9, 105.2, 180.3, 160.5]

heights = [140, 152, 175, 174, 172]

# apple banana cherry
print(fruits[:3])

# banana cherry ... blueberry
print(fruits[1:])

# "grape", "strawbery", "blueberry"
print(fruits[8:])

#"kiwi", "grape", "strawbery", "blueberry"
print(fruits[-5:-1])

# change apple with mango
fruits[0] ="mango"
print(fruits)

fruits[-1] ="blackberry"
print(fruits)

fruits[-3] ="wildcherry"
print(fruits)

#models    0  1  2  3     4     5     6     7      8      9  10     11
iprices = [0, 0, 0, 4990, 5990, 7990, 9990, 19990, 29990, 0, 45990, 53990]
print(iprices)


#+10.5%
for price in iprices:
  print(price+price * 0.105)

for i in range(len(iprices)):
  print(price+price * 0.105)

print(iprices)

