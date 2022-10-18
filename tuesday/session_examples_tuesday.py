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

text = "Hello World"

for currywurst in text:
    print(currywurst)


for number in range(11):
    print(number)

print('++++++++')

for number in range(5,11):
    print(number)

print('+++++++')

for whatever in range(2,27,2):
    print(whatever)


# Function


# Collections