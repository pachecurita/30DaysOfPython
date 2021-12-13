# Declare a function named evens_and_odds. It takes a positive integer as parameter and its counts number of evens and odds in the number.

def evens_and_odds(ran):
    total_evens = 0
    total_odds = 0
    for num in range(ran+1):
        if (num) % 2 == 0:
            total_evens += 1
        elif (num) % 2 != 0:
            total_odds += 1
    return total_evens, total_odds

evens, odds =evens_and_odds(100)
#print(evens, odds)

def factorial(num):
    if num > 0:
        if num == 1:
            return 1
        else:
            fact = 1
            for n in range(num):
                fact *= (n+1)
            return fact

#print(factorial(10))

def is_empty(arg):
    if len(arg) == 0:
        empty = True
    else:
        empty = False
    return empty

#print(is_empty([1]))

# 3 
def calculate_mean(lst):
    sum_num = 0
    for num in lst:
        sum_num += num
    mean = sum_num / len(list)
    return mean

def calculate_median(lst):
    lst.sort()
    if len(lst) % 2 != 0:
        median = lst[len(lst)//2]
    else:
        median = (lst[len(lst)//2] + lst[((len(lst)//2))-1]) /2
    return median

#print(calculate_median([1,2,3]))

def calculate_mode(lst):
    pass

def calculate_range(lst):
    pass

def calculate_variance(lst):
    pass

def calculate_std(lst):
    pass


