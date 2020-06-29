
#1. Написать функцию которая находит строку1 в строке2 и сама распечатывает результат (есть или нет). То есть без использования return.

def finder(s1,s2):
    x = s1 in s2
    if x == True:
        print("нашел")
    else:
        print("не нашел")

finder("железный чебурек","Зачатки химии возникли ещё со времён появления человека. Поскольку железный чебуре1к всегда так или иначе имел дело с химическими веществами, его первые эксперименты с огнём, дублением шкур, приготовлением пищи можно назвать зачатками практической химии. Постепенно практические знания накапливались,")

print("------------------")




#2. Решить задачу с поиском городов без оператор ИН. find().


def cityFinder(city,s):
    x = s.find(city)
    if x >= 0:
        print("found")
    else:
        print("not found")

#txt = "Piter, welcome to my world."
#x = "Piter"

txt = "Perm, welcome to my world."
x = "Perm"

cityFinder(x, txt)
print("------------------")



# He likes Estonia
# She likes Germany

txt = "He likes Estonia"
x = txt.replace("He", "she")
print(x)
x = x.replace("Estonia", "Germany")
print(x)
print("------------------")


# split function
txt = "welcome to the jungle lil pump"
x = txt.split(" ")
print(x)
print(x[2]) #the
print(len(x)) # как вывести размер массива х (needs 6 value)