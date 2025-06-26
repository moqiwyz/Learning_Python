weight = int(input("How much do you weigh? "))
unit = input("Please choose the unit: (L)bs or (K)g ")

if unit.upper() == "L":
 converted = weight * 0.45
 print(f"You are {converted} kilos.")
else:
 converted = weight / 0.45
 print(f"You are {converted} pounds.")