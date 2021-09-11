### Exercises: Level 2
# Write a code which gives grade to students according to theirs scores:
# 90-100, A
# 70-89, B
# 60-69, C
# 50-59, D
# 0-49, F

score = int(input('Enter your final score (0-100): '))
if 0 <= score < 50:
    print('Your final grade is: F.')
elif 50 <= score < 60:
    print('Your final grade is: D.')
elif 60 <= score < 70:
    print('Your final grade is: C.')
elif 70 <= score < 90:
    print('Your final grade is: B.')
elif 90 <= score <=100:
    print('Your final grade is: A.')
else:
    print('This score is invalid.')

input('Enter to continue...')
# Check if the season is Autumn, Winter, Spring or Summer. If the user input is: September, October or November, the season is Autumn. December, January or February, the season is Winter. March, April or May, the season is Spring June, July or August, the season is Summer
month = (input('Enter the actual month: ')).upper()
autumn = 'SEPTEMBEROCTOBERNOVEMBER'
winter = 'DECEMBERJANUARYFEBRUARY'
spring = 'MARCHAPRILMAY'
summer = 'JUNEJULYAUGUST'

if month in autumn:
    print('Its Autumn!')
elif month in winter:
    print('Its Winter!')
elif month in spring:
    print('Its Spring!')
elif month in summer:
    print('Its Summer!')
else:
    print('Invalid month.')


# The following list contains some fruits:
fruits = ['banana', 'orange', 'mango', 'lemon']
# If a fruit doesn't exist in the list add the fruit to the list and print the modified list. If the fruit exists print('That fruit already exist in the list')
fruit = input('Add a fruit: ').lower()

if fruit in fruits:
    print('That fruit already exist in the list.')
else:
    fruits.append(fruit)

print(fruits)