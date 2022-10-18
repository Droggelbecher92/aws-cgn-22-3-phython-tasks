from random import randint
# Recap Day 1

name = "Anna"

print(name)
#var = input("Please enter your name: ")

name.upper()

num = 5

# num = num + 5
num += 5
#type(var)
#int(var)


# Try some Operaterators
age = 17
living_in = "USA"

#You can also chain conditions
if not(age<16) and living_in=="GER":
    print("Here you go, beer")
    print("lkdfgjkl")
elif age==16:
    print("Only beer")    
else:
    print("TOO YOUNG!!")

# Loops

# while
# unknown ammount of loops

its_raining = True

while its_raining:
    print("Rain!")
    num = randint(1,100)
    if num==50:
        its_raining=False

seconds = 0

while seconds<60:
    print("Not a minute")
    print(seconds)
    if seconds==30:
        print("Halftime")
        seconds += 10
        continue
    if seconds==45:
        break
    seconds += 1
print("minute!")


# for
# known ammounts of loops
# works with iterables. So far we know Strings, but also very handy for Lists

text = "Hello World"

#Every Symbol in the string will be used
for currywurst in text:
    print(currywurst)


#With range() we can also set our loop 
for number in range(11):
    print(number)

print('++++++++')

for number in range(5,11):
    print(number)

print('+++++++')

for whatever in range(2,27,2):
    print(whatever)


# Function

def anyname():
    print("kjdfhg")


anyname()

def addition(currywurst, num2):
    return f"The additon is {currywurst+num2}"

print(addition(3,5))

sum = addition(5,7)

addition("B","A")


def fizzbuzz(number):
    if number%3==0 and number%5==0:
        print("FizzBuzz")
    elif number%3==0:
        print("Fizz")
    elif number%5==0:
        print("Buzz")
    else:
        print(number)


fizzbuzz(4)
fizzbuzz(15)





# Collections