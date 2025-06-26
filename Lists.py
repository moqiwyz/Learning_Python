names = ['John', 'Bob', 'Mosh', 'Sarah', 'Mary']
names[0] = "Jon"
print(names[0])
print(names[2:])


numbers = [3, 6, 2, 8, 20, 4, 10]
max = numbers[0]
for number in numbers:
    if number > max:
        max = number
print(max)