# Use for loop to iterate from 0 to 100 and print the sum of all numbers.
# The sum of all numbers is 5050.
sum_all = 0
for i in range(101):
    sum_all += i
print(f'The sum of all numers is {sum_all}.')
# Use for loop to iterate from 0 to 100 and print the sum of all evens and the sum of all odds.
sum_all_evens = 0
sum_all_odds = 0
for i in range(101):
    if i % 2 == 0:
        sum_all_evens += i
    else:
        sum_all_odds += i
# The sum of all evens is 2550. And the sum of all odds is 2500.
print(f'The sum of all evens is {sum_all_evens}. And the sum of all odds is {sum_all_odds}.')