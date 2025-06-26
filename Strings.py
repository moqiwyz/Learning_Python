message = '''
Hi John,

Here is our first email to you.

Thank you,

The Support Team
'''         # '''...''' or """...""" = multi-line strings
print(message)


course = 'Python for Beginners'
print(course[-1])       # [#] = index which starts from 0
print(course[0:3])      # index starting from -1 to 2, excluding 3
print(course[0:])       # prints from index 0 to the end
print(course[:5])       # print from index 0 to 4
another = course[:]
print(another)          # clone course


name = 'Jennifer'
print(name[1:-1])