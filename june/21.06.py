import re

#2. Определить есть ли в строке название городов Москва Питер Новосибирск?
x = "Очевидно, что действующая столица превосходит размерами и численностью свою северную подругу. На вопрос, " \
    "какой город больше – Москва "
x2 = "Очевидно, что действующая столица превосходит размерами и численностью свою северную подругу. На вопрос, " \
    "какой город больше –  "
r = re.findall(r'[^а-я](Москва|Питер) ', x2)

n = len(r)
print("r: "+str(n))

if n >= 1:
  print("Москва и Питер найдена")
else:
  print("города не найдены")
print("-------------------")


# Results about each city
txt = "Мос1ква: их мало даже на окраинах, но в центре больше чем в Питере. Ри?м называют Вечным городом"
x = "Москва" in txt
if x == True:
    print("Москва")
else:
    print("нет Москвы =(")
x = "Питер" in txt
if x == True:
    print("Питер")
else:
    print("нет Питера")
x = "Рим" in txt
if x == True:
    print("Рим")
else:
    print("нет Рима =(")

print("-------------------")

# Same task with function

def cityFinder(city, s):
    x = city in s
    if x == True:
        return city+": is found"
    else:
        return city+": is not found"

print(cityFinder("Москва", txt))
print(cityFinder("Питер", txt))
print(cityFinder("Рим", txt))
