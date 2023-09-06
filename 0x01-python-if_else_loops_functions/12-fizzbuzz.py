#!/usr/bin/python3
def fizzbuzz():
    for results in range(1, 101):
        if results % 3 == 0 and results % 5 == 0:
            print("FizzBuzz", end='')
        elif results % 3 == 0:
            print("Fizz", end='')
        elif results % 5 == 0:
            print("Buzz", end='')
        else:
            print(results, end='')

        print(" ", end='')
