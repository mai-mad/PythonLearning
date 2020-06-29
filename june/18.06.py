import re

txt = "Ilya hates windows"
print(txt)
x = txt.replace("hates", "loves")
print(x)
x = x.replace("windows", "MACos")
print(x)

x = x.upper()
print(x)

x = x.lower()
print(x)

# Phonde code -> City
phone = "(8422) 41-23-93" # krasnodar perm ulyanovsk

x = phone.find("(495)")
if x >= 0:
 print("Moscow")

x = phone.find("(812)")
if x >= 0:
 print("Piter")

x = phone.find("(861)")
if x >= 0:
 print("Krasnodar")

x = phone.find("(342)")
if x >= 0:
 print("Perm")

x = phone.find("(8422)")
if x >= 0:
 print("Ulyanovsk")


# Создать строку и определить есть ли в ней предлоги "в, без, до, из"
y = "Производные бе предлоги образовались  более позднее время от слов  других частей речи и подразделяются на"

r = re.findall(r'[^а-я](в|без|до|из|от) ', y)

n = len(r)  # n - это количество предлогов
print ("r: "+str(len(r)))

if n >= 1:
 print("предлоги найдены")
else:
 print("предлоги не найдены")



# Method Split
a = "is,red,This" # This is red
m = a.split(",")
print(m) # returns ['Hello', ' World!']

# print Ivan
#print(m[0])
# print Dima
#print(m[1])

# print This is red!
print(m[2], m[0], m[1])


# Operator "in"
txt = "The rain in Spain stays mainly in the plain"
if "Rediska" in txt:
    print("OK")
else:
    print("not OK")


# Concatinations
a = "Hello"
b = "World"
c = a + " " + b + "!"

# Hello World! Hello Ivan!
print(c + " Hello Ivan!")


age = 36
txt = "My name is John, I am " + str(age)
print(txt)