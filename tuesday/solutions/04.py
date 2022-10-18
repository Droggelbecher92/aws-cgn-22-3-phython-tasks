
#  ----------
#    PART 1
#  ----------
word = "supercalifragilisticexpialidocious"

# Write a for loop that prints out each character in the above "word" variable
for letter in word:
    print(letter)
    
# Write a while loop that does the same thing!
counter = 0
while counter < len(word):
    print(word[counter])
    counter += 1

#  ----------
#    PART 2
#  ----------
# Write a while loop that prints the even numbers from 100 to 140 (including 140)
counter = 100
while counter<=140:
    if counter%2==0:
        print(counter)
    counter += 1

# Write a for loop that does the same thing (with range())
for number in range(100,141,2):
    print(number)

#  ----------
#    PART 3
#  ----------
# Write a loop that asks a user to input the passphrase "sillygoose" and keeps asking them to do so until they comply:

correct_passphrase = False
while not(correct_passphrase):
    passphrase = input("Enter the passphrase:")
    if passphrase=="sillygoose":
        print("YOU SHALL PASS!")
        correct_passphrase = True
    else:
        print("Try again....")