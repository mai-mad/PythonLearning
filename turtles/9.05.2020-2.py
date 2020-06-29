import random

# ПК загадывает число от 0 до 10
# Игрок вводит вариант
# Сообщиение правильно неправильно
# *** Подсчитать кол-во попыток
#

game = "yes"
n = random.randint(1, 5)
count = 1


while game == "yes":
    x = int(input("Your choice: "))
    if x < n:
        print("your number less than mine")
    if x > n:
        print("your number bigger than mine")
    if n == x:
        print("you're right")
        print("attempts: " + str(count))
        if count == 1:
            print("you're awesome")
        elif count == 5:
            print("YOU ARE NOTHING!!!!")
        game = "no"
    else:
        print("You are looser!!!!!!!!")
        count = count + 1

print("Right number"+str(n))