course = 'Python for Beginners'
print(len(course))      # general purpose in-built function (including the spaces)
print(course.upper())    # object.method() - methods need objects. Methods return.
print(course.lower())
print(course)
  
# index of the first appearance of the character, also it's CASE SENSITIVE! If the result is -1, it means it doesn't exist.
print(course.find('n'))

# you can search for a word, and the result will be the index where the word starts 
print(course.find('Beginners'))

# replace A to B (CASE SENSITIVE!)
print(course.replace('Beginners', 'Absolute Beginners'))
print(course.replace('P', 'J'))

# nothing happens because the case doesn't match
print(course.replace('beginners', 'Absolute Beginners'))

# boolean expression - the result will be True or False (CASE SENSITIVE!). 'in' operator is a boolean expression.
print('Python' in course)

# .title() capitalizes the first letter of every word and lower case the rest