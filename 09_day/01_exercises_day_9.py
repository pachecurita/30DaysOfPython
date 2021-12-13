# Exercises: Level 1
#Get user input using input(“Enter your age: ”). If user is 18 or older, give feedback: You are old enough to drive. If below 18 give feedback to wait for the missing amount of years.
my_age = int(input('Enter your age: '))

if 100 > my_age >= 18:
    print('You are old enough to learn to drive.')
elif 0 < my_age < 18:
    age_of_difference = 18 - my_age
    print(f'You need {age_of_difference} more years to learn to drive.')
else:
    print('Invalid age.')

# Compare the values of my_age and your_age using if … else. Who is older (me or you)? Use input(“Enter your age: ”) to get the age as input. You can use a nested condition to print 'year' for 1 year difference in age, 'years' for bigger differences, and a custom text if my_age = your_age.
your_age = int(input('Enter the age of your partner : '))
age_diff = my_age - your_age

if age_diff > 0:
    if age_diff == 1:
        print(f'You have {abs(age_diff)} years more than your partner.')
    else:
        print(f'You have {abs(age_diff)} years more than your partner.')
elif age_diff < 0:
    if age_diff == -1:
        print(f'Your partner has {abs(age_diff)} years more than you.')
    else:
        print(f'Your partner has {abs(age_diff)} years more than you.')
else:
    print(f'You have the exactly same age: {my_age} years.')


input('Enter to continue. . . ')
# Get two numbers from the user using input prompt. If a is greater than b return a is greater than b, if a is less b return a is smaller than b, else a is equal to b.
num_one = int(input('Enter number one: '))
num_two = int(input('Enter number two: '))

if num_one > num_two:
    print(f'{num_one} is greater than {num_two}.')
elif num_one < num_two:
    print(f'{num_one} is smaller than {num_two}.')
else:
    print(f'{num_one} is equal to {num_two}.')