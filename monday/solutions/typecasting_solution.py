print("""
WELCOME TO OUR USELESS STORE!
*****************************
""")

item = input("what item are you purchasing?")
price = input("what is the price of " + item + "?")
ammount = input("how many " + item + " are you buying?")



total = str(int(ammount) * float(price))

print("Added " + ammount + " " + item + "(s) to shopping cart")
print("Subtotal: $" + total)
