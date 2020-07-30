""""
ilya_has = ["iphone", "imac"] # imac iphone

# solution:
ilya_has.remove("iphone")
#ilya_has.insert(1,"iphone")
ilya_has.append("iphone")

print(ilya_has)"""

# iDedushkina  ipad iBabushkina iIlya imac
ilya_has = ["ibook", "iphone", "imac", "ipad", "ipod"]
del ilya_has[4]
del ilya_has[2]
del ilya_has[1]
del ilya_has[0]
ilya_has.append("iBabushkina")
ilya_has.append("iIlya")
ilya_has.append("imac")
ilya_has.insert(0, "iDedushkina")
print(ilya_has)

fruits = ["apple", "banana", "cherry"]
print(fruits[0:2]) # a b

f1 = ("apple", "abricos")
f2 = ("banana", "becon")
f3 = list(f1 + f2)

print(f3)
f3[0]="meat"
print(f3)