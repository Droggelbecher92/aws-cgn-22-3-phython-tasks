# Last FizzBuzz Challenge, I promise! You can use the logic 
# from the other tasks, but if you want to train, start from scratch :)
# Write two functions:
#   - the first will fizzbuss from 1-100 without an argument
#   - the second will take one number as an argubent, to check for a fizzbuzz
#BOUNS:
#   - The function gets two argument, a starting number and a final number. 
#     Do the fizzbuzz for every number in this range.

def fizzbuzz_auto():
    for number in range(1,101):
        if number%3==0 and number%5==0:
            print("FizzBuzz")
        elif number%3==0:
            print("Fizz")
        elif number%5==0:
            print("Buzz")
        else:
            print(number)


def fizzbuzz(number):
    if number%3==0 and number%5==0:
        print("FizzBuzz")
    elif number%3==0:
        print("Fizz")
    elif number%5==0:
        print("Buzz")
    else:
        print(number)

def fizzbuzz_range(start,stop):
    for number in range(start,stop+1):
        if number%3==0 and number%5==0:
            print("FizzBuzz")
        elif number%3==0:
            print("Fizz")
        elif number%5==0:
            print("Buzz")
        else:
            print(number)

fizzbuzz(15)
fizzbuzz_range(5,15)
fizzbuzz_auto()