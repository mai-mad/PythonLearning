#Paper Scissors Stone
import random

# варианты что можно выбрать
cases = ['b', "n", "k"]

# загадывает ПК
pc = cases[ random.randint(0,2) ]


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
print(pc)
'''
00+
11+
22+
01+
02+
10+
12+
20+
21+
'''