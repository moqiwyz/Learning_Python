'''
birth_year = input('Birth year: ')
print(type(birth_year))           # type = to tell you if it is str/int/float/bool....
age = 2019 - int(birth_year)      # pass birth_year string to the int function
print(type(age))
print(age)
'''

weight_lbs = input('How much do you weigh in pounds? ')
weight_kg = int(weight_lbs) * 0.453
print(weight_kg)