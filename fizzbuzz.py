# -*- encoding: utf-8 -*-
x=raw_input("Vnesi številko med 1 in 100:  ")
x=int(x)

for x in range(1, x):
    if x%5==0 and x%3==0:
        print("FizzBuzz")
    elif (x%5) ==0:
        print("Buzz")
    elif x%3==0:
        print("Fizz")
    else:
        print(str(x))


