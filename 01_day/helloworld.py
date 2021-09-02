# DAY 1 / EXERCISES LEVEL 2

# 1. Check the python version you are using:
#    Im using the version 3.9.6 of Python.

# 2. Do the operations with the operands: 3 and 4.
print(3 + 4) # addition(+)
print(3 - 4) # subtraction(-)
print(3 * 4) # multiplication(*)
print(3 % 4) # modulus(%)
print(3 / 4) # division(/)
print(3 ** 4) # exponential(**)
print(3 // 4) # floor division(//)

# 3. Write strings.
print('My name is Paula Huichacura.')
print("My mother's name is Ana, my dad's Jose and my siblings Aylin and Jose.")
print('Im from Chile.')
print('Im enjoying 30 days of python.')

# 4. Check the data types of the different data:
print(type(10))
print(type(9.8))
print(type(3.14))
print(type(4-4j))
print(type(['Asabeneh', 'Python', 'Finland']))
print(type('Paula Huichacura'))
print(type("My mother's name is Ana, my dad's Jose and my siblings Aylin and Jose."))
print(type('Chile'))

# EXERCISES LEVEL 3:
#1. Write an example for different Python data types:
print(1) # Number> Int
print(17.5) # Number > Float
print(1+4j) # Numer > Complex
print('This is a string') # String
print(True) # Boolean
print(['Paula', 'Jose', 'Ana', 'Aylin']) # List
print((3.14, 2.718, )) # Tuple
print({1, 2.2, 3, 4}) # Set
print({'name':'Paula', 'nickname':'pachecurita'})

# 2. Find an Euclidian distance between (2, 3) and (10, 8).
'''
To solve this exercise I had to look up what the Eucledian distance was. 
This is defined in mathematics as the ordinary distance that exists between two points, 
which is deduced from the Pythagorean theorem. 
Having point A(x1,y1) and point B(x2,y2) the formula to know the distance between those two points:
Distance between A and B = Square root of ((x2 - x1)^2 + (y2 - y1)^2).

The square root of a number is nothing more than the number raised to 0.5, 
so I will calculate it using this method.
'''

print('The distance between (2,3) and (10,8) is:')
print(((10 - 2)**2 + (8 - 3)**2)**0.5)
