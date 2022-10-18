player_1 = input("Enter name Player 1:")
player_2 = input("Enter name Player 2:")

running = True

while running:
    sticks = 13
    current_player=player_1
    while sticks > 0:
        pipes = "|"
        for num in range(sticks):
            pipes += " |"
        print(pipes)
        print(f"There are {sticks} matches left.")
        valid_input = False
        while not(valid_input):
            how_many = int(input(f"How many do you take, {current_player}: "))
            if how_many<4 and how_many>0:
                break
            print("Not a valid input")
        sticks -= how_many
        if sticks<=0:
            break
        if current_player==player_1:
            current_player=player_2
        else:
            current_player=player_1
    print(f"{current_player} wins!!!")
    again = input("Wanna play again? 'q' to quit:")
    if again== "q":
        print("Thank you for playing!")
        running=False