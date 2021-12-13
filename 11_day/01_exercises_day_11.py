from math import sqrt
# 1
def add_two_numbers(num1, num2):
    return num1 + num2

# 2
def area_of_circle(radio):
    PI = 3.14
    return PI * radio**2

# 3
def add_all_nums(*nums):
    suma = 0
    for num in nums:
        if type(num) != type(1):
            print(f'El valor {num} no es un número, por lo que se ignorará.')
        else:
            suma += num
    return suma

# 4
def convert_celcius_to_fahrenheit(temp_in_C):
    temp_in_F = (temp_in_C * (9/5)) + 32
    return temp_in_F

# 5
def check_season(month):
    month_low = month.lower()
    if month_low == 'december' or month_low == 'january' or month_low == 'february':
        return 'Summer'
    elif month_low == 'march' or month_low == 'april' or month_low == 'may':
        return 'Autumn'
    elif month_low == 'june' or month_low == 'july' or month_low == 'august':
        return 'Winter'
    elif month_low == 'september' or month_low == 'october' or month_low == 'november':
        return 'Spring'
    else:
        return 'Invalid month'


def calculate_slope(linear_eq):
    pass


def solve_quadratic_eqn(a, b, c):
    if ( b**2 - (4* a * c) ) >= 0:
        x1 = (-b + sqrt(b**2 - (4* a * c)))/2*a
        x2 = (-b - sqrt(b**2 - (4* a * c)))/2*a
        return f'The solutions of {a}x^2 + {b}x + {c} are X1: {x1} and X2: {x2}'
    else:
        return f'The solutions of {a}x^2 + {b}x + {c} are complex roots'

#print(solve_quadratic_eqn(10, 5, 8))
#print(solve_quadratic_eqn(-1, 6, 5))

def print_list(list):
    for i in list:
        print(i, end=' ')

#print_list([1,2,3,4,5,6,'213'])


def reverse_list(initial_list):
    reversed_list = []
    for i in range(len(initial_list)):
        popp = initial_list.pop()
        reversed_list.append(popp)
    return reversed_list

#print(reverse_list([1,2,3,4,5]))

# 10
def capitalize_list_items(list_of_items):
    items_capitalized = []
    for item in list_of_items:
        new_item = item.capitalize()
        items_capitalized.append(new_item)
    return items_capitalized

#print(capitalize_list_items(['hola', 'jaja', 'jjejeje']))

## 11
def add_item(list_numbers, num):
    list_numbers.append(num)
    return list_numbers

print(add_item([1,2,3], 4))

## 12
def remove_item(list_numbers, num):
    for n in list_numbers:
        if n == num:
            list_numbers.pop(list_numbers.index(n))
    return list_numbers

print(remove_item([1,2,3], 4))

## 13
def sum_of_numbers(ran):
    sum_of_all = 0
    for i in range(ran+1):
        sum_of_all += i
    return sum_of_all

print(sum_of_numbers(10))

#14
def sum_of_odds(rang):
    sum_odds = 0
    for num in range(rang+1):
        if num % 2 != 0:
            sum_odds += num
    return sum_odds

print(sum_of_odds(4))

def sum_of_evens(rang):
    sum_evens = 0
    for num in range(rang+1):
        if num % 2 == 0:
            sum_evens += num
    return sum_evens

print(sum_of_evens(4))
