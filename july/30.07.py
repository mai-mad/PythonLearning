fruits = ["apple", "banana", "apple"]
#print(fruits)
fruits.append("apple")
#print(fruits)

# create set from 1 element the add couple vegetables
veg = {"cucumber"}
veg.add("tomato")
veg.add("potato")
veg.add("potato")

veg.update(["corn", "carrot", "tomato", "pumpkin"]) # 6

# number of veg:
print(len(veg))

# number of fruits
print(len(fruits))

# remove from veg: carrot pumpkin
veg.remove("pumpkin")
veg.remove("carrot")
print("veg:")
print(veg)
#print(len(veg))


veg2 = {"cabachok", "petrushka", "onion", "garlik"}
print("veg2: ")
print(veg2)

# join two sets of vegs to third set
veg3 = veg.union(veg2)
print ("veg3:")
print(veg3)

veg4 = veg3.union(veg)
print ("veg4:")
print(veg4)

igoods = ["ipod", "iIlya", "iphone", "iphone", "ipad", "iwatch", "iwatch"]
iset = set(igoods)
print(len(iset)) # 5


ilyahas = {"ipod", "ipad", "imac", "macbook pro", "iwatch 3", "iwatch 4", "airpods", "iphone"}
dimahas = {"iphone", "iwatch 5", "macbook", "airpods", "ipod"}

# Which ithings has Ilya and Dima simuntnijsldfhyaosydfas
z = ilyahas.difference(dimahas)
print(z)