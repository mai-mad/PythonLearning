print ("cake")

# 1 2 3 4 ... 9
for x in range(1, 10):
  print(x)
print("end.")


for x in range(9):
  print(x+1)
print("end.")


# 0 2 4 6
for x in range(0, 7, 2):
  print(x)
print("end.")


# from -3 till 3 with step 3

for x in range(-3, 4, 3):
  print(x)
print("end.")


# sum from 2 till 9 with step 2 (2+4+6+8)
sum = 0
for i in range(2, 9, 2):
    sum = sum + i
print(sum+1)


# mul 1*2*3*...*10 = 3m
mul = 1
for i in range(1, 11, 1):
    mul = mul * i
print(mul)