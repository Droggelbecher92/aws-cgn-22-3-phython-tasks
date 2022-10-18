from random import randint

how_many = int(input("How many dice are we rolling?"))
sides = int(input("How many sides on each die?"))

running = True

while running:
    output = "|"
    for num in range(0,how_many-1):
        eyes = randint(1,sides)
        output = f"{output}{eyes}|"
    print(output)
    again = input("Again? 'q' to quit:")
    if again=="q":
        running=False