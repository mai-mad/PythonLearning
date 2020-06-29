#Paper Scissors Stone
import random

# варианты что можно выбрать
cases = ['b', "n", "k", "s", "l"]


game = "yes"

while game == "yes":
    # загадывает ПК
    pc = cases[random.randint(0, 4)]

    # player choice
    pl = input("Your choice: ")

    if pc == pl:
        print("Draw")
    elif pc == 'b' and pl == 'n':
        print("Player Wiiiiiin")
    elif pc == 'n' and pl == 'b':
        print("pc wiiiiiiin")
    elif pc == 'b' and pl == 'k':
        print("pc wiiiiin")
    elif pc == 'n' and pl == 'k':
        print("Player win")
    elif pc == 'k' and pl == 'b':
        print("Player win")
    elif pc == 'k' and pl == 'n':
        print("pc win")
    elif pc == 'b' and pl == 's':
        print("Player win")
    elif pc == 'b' and pl == 'l':
        print("Player win")
    elif pc == 'n' and pl == 's':
        print("Player win")
    elif pc == 'n' and pl == 'l':
        print("pc win")
    elif pc == 'k' and pl == 's':
        print("Player win")
    elif pc == 'k' and pl == 'l':
        print("pc win")
    elif pc == 's' and pl == 'b':
        print("Player win")
    elif pc == 's' and pl == 'n':
        print("pc win")
    elif pc == 's' and pl == 'k':
        print("pc win")
    elif pc == 's' and pl == 'l':
        print("Player win")
    elif pc == 'l' and pl == 'b':
        print("pc win")
    elif pc == 'l' and pl == 'n':
        print("pc win")
    elif pc == 'l' and pl == 'k':
        print("Player win")
    elif pc == 'l' and pl == 's':
        print("pc win")
    print(pc)

    game = input("one more time?")

print("Game Over")