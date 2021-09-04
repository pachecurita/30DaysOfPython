# 6. Get length and width of a rectangle using prompt. Calculate its area (area = length x width) and perimeter (perimeter = 2 x (length + width))
length_rectangle = float(input('Enter length of rectangle: '))
width_rectangle = float(input('Enter width of rectangle: '))
area_rectangle = length_rectangle * width_rectangle
print('The rectangle area is: ', area_rectangle)
perimeter_rectangle = 2 * (length_rectangle + width_rectangle)
print('The rectangle perimeter is: ', perimeter_rectangle)

# 7. Get radius of a circle using prompt. Calculate the area (area = pi x r x r) and circumference (c = 2 x pi x r) where pi = 3.14.
radius_circle = float(input('Enter radius of a circle: '))
PI = 3.14
area_circle = PI * (radius_circle**2)
print('The area of the circle is: ', area_circle)
circumference_circle =  2 * PI * radius_circle
print('The circumference of the circle is: ', circumference_circle)

# 8. Calculate the slope, x-intercept and y-intercept of y = 2x -2
y_intercept_08 = 2 - 2
x_intercept_08 = 2 / 2
slope_08 = y_intercept_08/x_intercept_08

# 9. Slope is (m = y2-y1/x2-x1). Find the slope and Euclidean distance between point (2, 2) and point (6,10)
slope_09 = (10 - 2)/ (6 - 2)
euc_distance_09 = ((10-2)+(6-2))**0.5

# 10. Compare the slopes in tasks 8 and 9.
print('Is slope of exercise 08 equal to 09? ', slope_08 == slope_09)

# 11. Calculate the value of y (y = x^2 + 6x + 9). Try to use different x values and figure out at what x value y is going to be 0.
x_value = float(input('Enter a x value: '))
y_value = (x_value**2) + (6 * x_value) + 9
print('When x = ', x_value, ' the y value is: ', y_value)

# 12. Find the length of 'python' and 'dragon' and make a falsy comparison statement.
lenght_python = len('python')
lenght_dragon = len('dragon')
falsy_comparation = lenght_python == lenght_dragon

# 13. Use and operator to check if 'on' is found in both 'python' and 'dragon'
on_in_python = 'on' in 'python'
on_in_dragon = 'on' in 'dragon'
print("Is 'on' in 'python'? ", on_in_python,". Is 'on' in 'dragon'? ", on_in_dragon)

# 14. I hope this course is not full of jargon. Use in operator to check if jargon is in the sentence.
sentence = 'I hope this course is not full of jargon.'
jargon_in_sentence = 'jargon' in sentence

print(f"Is 'jargon' in the sentence: '{sentence}'? ", jargon_in_sentence)
# 15. There is no 'on' in both dragon and python
no_on_python = 'on' not in 'python'
no_on_dragon = 'on' not in 'dragon'

# 16. Find the length of the text python and convert the value to float and convert it to string
lenght_python_16 = len('python')
lenght_float_python = float(lenght_python_16)
txt_len_python =  str(lenght_float_python)

# 17. Even numbers are divisible by 2 and the remainder is zero. How do you check if a number is even or not using python?
num = int(input('Enter int number: '))
is_even = (num % 2) == 0
print('Is your number an even? : ', is_even)

# 18. Check if the floor division of 7 by 3 is equal to the int converted value of 2.7.
floor_div = 7 // 3
converted_int = int(2.7)
is_equal = floor_div == converted_int
print('Is 7//3 equal to 2.7 converted to int? ', is_equal)

# 19. Check if type of '10' is equal to type of 10
check_txt_10 = type('10')
check_int_10 = type(10)
are_equal_type = check_int_10 == check_txt_10
print("Is '10' equal to 10 in Python? ", are_equal_type)

# 20. Check if int('9.8') is equal to 10
# check_int_98 = int('9.8') 
#   It happens an error> ValueError: invalid literal for int() with base 10: '9.8'
#   There are two solutions: Use float('9.8') or convert the floating number 9.8 to int.
check_int_98 = float('9.8') # Option 1
# check_int_98              # Option 2
are_equal = check_int_98 == 10
print('Is the float of "9.8" equal to 10? ', are_equal)
