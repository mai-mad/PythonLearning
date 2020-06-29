import random

game = "yes"
n = random.randint(1, 5)
count = 1
while game == "yes":
    x = int(input("Your choice:"))
    if x < n:
        print("Your number less than mine")
    elif x > n:
        print("Your number bigger than mine")
    elif n == x:
        print("you're right")
        print("attempts"+ str(count))
        if count == 1:
            print("you're awesome!")
        elif  count == 5:
            print("YOU ARE STUPID!!!")

        else:
            print("you are dumb!")

        game = "no"
    count = count + 1
