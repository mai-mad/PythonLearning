import random
import arcade

n = random.randint(1, 10)
print("n = "+str(n))
x = random.randint(1, 10)
print("x = "+str(x))
if x < n:
    print("n bigger than x")
elif x > n:
    print("x bigger than n")
elif n == x:
    print("draw")
