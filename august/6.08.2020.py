print ("while task")

i = 1
j = 0
while i > j: # i=2 > j=1
    print(i+j)
    i=j+1 # i = 1 + 1, i = 2
    if j == i: # 1 == 2
        break
    i+=1 # i = 2
    j+=1 # j = 1

# output: 1 3 5 7 9 11 ...


# 0 5 11 15 20 26 30 35 41 45 50 56

# 0 3 7 9 12 16 18 +
# 0 3 7 9 12 16 18