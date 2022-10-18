# write a function that prints out if the the division of two numbers has a remainder

def has_remainder(num1, num2):
    remain = num1 % num2
    print(f"Remainder: {remain}")
#write a function that returns a given string in reverse order

def encrypt(text_to_encrypt):
    return text_to_encrypt[::-1]
print(encrypt("abcde"))
#write a function that takes a string and returns the snakecase version of this string
# Example: This is a file => this_is_a_file

def snakecaser(text):
    return text.lower().replace(" ","_")

print(snakecaser("This is a file"))