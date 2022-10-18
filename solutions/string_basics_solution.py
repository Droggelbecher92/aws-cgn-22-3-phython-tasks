first = "Carl"
last = "Klozenheimer"

# - Create a variable called "full_name" that combines first and last with a space between them.  
# - Print it out
full_name = first + " " + last
print(full_name)

# - Create an "initials" variable that holds the first character of first followed by the first character of last. 
# - Print it out
initals = first[0] + last[0]
print(initals)


# - Create an "initials_2" variable that holds the first character of first followed by the first character of last, with periods after each letter!
# - Print it out
initals_2 = first[0] + "." + last[0] + "."
print(initals_2)


# Create a "nickname" variable that holds the first 4 characters of "last" (use a slice)
# Print it out 
nick = last[0:4]
print(nick)

# BONUS:
# Create a new file where you ask for the age of the user (in years, try a float if 
# you want to) and print out his age in days. (Ignore the leap year)

age = input("How old are you?")
age_in_days = int(age) * 365
print("You are "+str(age_in_days)+" days old")