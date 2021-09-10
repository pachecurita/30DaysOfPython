# Exercises: Level 2
# 1. The following is a list of 10 students ages:
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

# Sort the list and find the min and max age
ages.sort()
age_min = ages.pop(0)
age_max = ages.pop()
print('Min age is: ', age_min)
print('Max age is: ', age_max)
# Add the min age and the max age again to the list
ages.append(age_min)
ages.insert(-2, age_max)
ages.sort()
print('Lenght ages:', len(ages))
print('Ages: ', ages)
# Find the median age (one middle item or two middle items divided by two)
if len(ages) % 2 == 0:
    median_age = (ages[len(ages)//2] + ages[(len(ages)//2)+1]) / 2
else:
    median_age = ages[len(ages)//2]
print('Median age is: ', median_age)
# Find the average age (sum of all items divided by their number )
# age_sum = 0
# for age in ages:
#     age_sum += age
age_sum = sum(ages)
average_age = age_sum / len(ages)
print('Average age is: ', average_age)
# Find the range of the ages (max minus min)
range_age = age_max - age_min
print('Range age is: ', range_age)
# Compare the value of (min - average) and (max - average), use abs() method
min_average =  abs(age_min - average_age)
max_average =  abs(age_max - average_age)
compare_min_max = min_average == max_average
print('Is the distance from min to average equal from max to average? ', compare_min_max)
