# How nested loops work: outer loop → inner loop runs fully → outer loop advances → inner loop runs again
for x in range(4):  # 4 is exclusive
    for y in range(3):  # 3 is exclusive
        print(f"({x}, {y})")



numbers = [5, 2, 5, 2, 2]
for number in numbers:
        print('x' * number)




numbers = [5, 2, 5, 2, 2]
for x_count in numbers:
    output=''
    for count in range(x_count):
        output += 'x'
    print(output)