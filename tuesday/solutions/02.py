from curses.ascii import isdigit


number = input("Please enter your number:")

if number.isdigit:
    number = int(number)
    if number%3==0 and number%5==0:
        print("FizzBuzz")
    elif number%3==0:
        print("Fizz")
    elif number%5==0:
        print("Buzz")
    else:
        print(number)   
else:
    print("Please enter a number")
