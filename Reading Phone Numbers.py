phone = input("Please enter your phone number: ")

digits_mapping = {
    "0": "O",
    "1": "One",
    "2": "Two",
    "3": "Three",
    "4": "Four",
    "5": "Five",
    "6": "Six",
    "7": "Seven",
    "8": "Eight",
    "9": "Nine"
}

output = ""
for ch in phone:
    output += digits_mapping.get(ch, "!") + " "
print(output)