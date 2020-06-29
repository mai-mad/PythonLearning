# input and output data
def example1():
    # Вывод на экран
    print(2+2)

    # Ввод данных с клавиатуры
    name = input("Your name: ")
    print("Your name is " + name) # добавление одной строки к другой

    age = input("Your age: ")
    print("Your age is " + age)

# simple calc
def example2():
    x = input("x: ") #2
    y = input("y: ") #2
    print(x+y)              #result: 22 (very strange)
    print(int(x) + int(y))  #result: 4 (very normal)

# ask user his age and say him his age in 1 year
def example3():
    age = input("Your age: ")
    print("Your age is " +str(int(age) + 3))

# ask user his age and age of his friend. Print sum of their ages.
def example4():
    age1 = input("Your age: ")
    print("Your age is " + age1)
    age2 = input("Your friend's age: ")
    print("his age is " + age2)
    print("sum of your ages: " +str(int(age1)+int(age2)))

# https://www.w3schools.com/python/python_getstarted.asp (We've stayed here)

#example1()
#example2()
#example3()
example4()