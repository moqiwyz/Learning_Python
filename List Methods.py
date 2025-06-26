numbers = [5, 2, 1, 7, 4]


numbers.append(20)  # adding a number at the end of the list
print(numbers)


numbers.insert(0, 10)   # the first number is index, the second number is the number you'd like to add
print(numbers)


numbers.remove(5)
print(numbers)


numbers.index(1)
print(numbers.index(1))


print(50 in numbers)    # True / False


numbers = [5, 2, 1, 7, 4, 5]
print(numbers.count(5))


numbers = [5, 2, 1, 7, 4, 5]
numbers.sort()   # sort method doesn't take any values / None = absence of a value / sort numbers in ascending order
numbers.reverse()  # sort numbers in descending order
print(numbers)


numbers = [5, 2, 1, 7, 4, 5]
numbers2 = numbers.copy()  # .copy() copies the list, and even if you make some chages in numbers, it won't impact numbers2
numbers.append(10)
print(numbers2)



numbers.pop()   # pop removes the one at the end of the list
print(numbers)


numbers.clear()
print(numbers)