# 21. Write a script that prompts the user to enter hours and rate per hour. Calculate pay of the person?
hours_worked = float(input('Enter your hours worked: '))
rate_per_hour = float(input('Enter the rate per hour: '))
pay_of_person = hours_worked * rate_per_hour
print('If you worked ', hours_worked, ' then your get ', pay_of_person, ' usd.')