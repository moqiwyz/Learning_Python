'''
if temperature is greater than 30
    it's a hot day
otherwise if it's less than 20
    it's a cold day
otherwise
    it's neither not nor cold
'''

temperature = 35
if temperature > 30:
    print("It's a hot day.")
else:
    print("It's not a hot day.")




name = input("What's your name? ")

if len(name) < 3:
    print("Name must be at least characters.")
elif len(name) > 50:
    print("Name can be a maximum of 50 characters.")
else:
    print("Name looks good!")
