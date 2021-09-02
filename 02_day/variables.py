# Day 2: 30 Days of python programming

# Exercises Level 1:
first_name = 'Paula'
last_name = 'Diaz'
full_name = first_name + ' ' + last_name
country = 'Chile'
city = 'Santiago'
age = 23
year = 2021
is_married = False
is_True = True
is_light_on = True
day_birthday, month_birthday, year_birthday = 25, 7, 1998

# Exercises Level 2:
# 1. Check the data type of all your variables using type() built-in function.
print('The type of ', first_name, ' is ', type(first_name))
print('The type of ', last_name, ' is ', type(last_name))
print('The type of ', full_name, ' is ', type(full_name))
print('The type of ', country, ' is ', type(country))
print('The type of ', city, ' is ', type(city))
print('The type of age: ', age, ' is ', type(age))
print('The type of year:', year, ' is ', type(year))
print('The type of  is_married: ', is_married, ' is ', type(is_married))
print('The type of is_True: ', is_True, ' is ', type(is_True))
print('The type of is_light_on: ', is_light_on, ' is ', type(is_light_on))

# 2. Using the len() built-in function, find the length of your first name.
print('The length of my first name: ', first_name, ' is ', len(first_name))

# 3. Compare the length of your first name and your last name.
print(first_name, ' is ', len(first_name), ' vs ', last_name, ' is ', len(last_name))

'''
4. Declare 5 as num_one and 4 as num_two
        Add num_one and num_two and assign the value to a variable total
        Subtract num_two from num_one and assign the value to a variable diff
        Multiply num_two and num_one and assign the value to a variable product
        Divide num_one by num_two and assign the value to a variable division
        Use modulus division to find num_two divided by num_one and assign the value to a variable remainder
        Calculate num_one to the power of num_two and assign the value to a variable exp
        Find floor division of num_one by num_two and assign the value to a variable floor_division
'''
num_one = 5
num_two = 4
total = num_one + num_two
diff = num_one - num_two
product = num_two * num_one
division = num_one / num_two
remainder = num_two % num_one
exp = pow(num_one, num_two)
floor_division = num_one // num_two

'''
5. The radius of a circle is 30 meters.
        Calculate the area of a circle and assign the value to a variable name of area_of_circle (pi * r^2)
        Calculate the circumference of a circle and assign the value to a variable name of circum_of_circle
        Take radius as user input and calculate the area.
'''
# radius_circle = 30 #
radius_circle = float(input('Insert circle radius: '))
PI = 3.14
area_of_circle = radius_circle * (PI)^2
circum_of_circle = 2 * PI * radius_circle

print('The area and the circum of a circle of radius: ', radius_circle, ' is ', area_of_circle, ' and ', circum_of_circle, ' respectively.' )

# 6. Use the built-in input function to get variables and store the value.
first_name_input = input('First name: ')
last_name_input = input('Last name: ')
country_input = input('Country: ')
age_input =  int(input('Age: '))

# 7. Run help('keywords') in Python shell to check for the Python reserved words (Done)
