# 22. Write a script that prompts the user to enter number of years. Calculate the number of seconds a person can live. Assume a person can live hundred years
age_user = int(input('Enter your age: '))
seconds_of_life = age_user * 365 * 24 * 60 * 60
print('You have lived ', seconds_of_life, ' seconds.')