# Exercises: Level 3
input('# Go to the data folder and use the countries.py file. Loop through the countries and extract all the countries containing the word land.')
from countries import countries

for country in countries:
    if 'land' in country:
        print(country)

input("# This is a fruit list, ['banana', 'orange', 'mango', 'lemon'] reverse the order using loop.")

fruit_list = ['banana', 'orange', 'mango', 'lemon']
fruit_list_reversed = []

for i in fruit_list:
    fruit_list_reversed.insert(0, i)

print(fruit_list_reversed)

input(' # Go to the data folder and use the countries_data.py file.\n1. What are the total number of languages in the data')
from countries_data import countries_data

total_languages = 0
language_lst = []
for country in countries_data:
    for key in country:
        if key == 'languages':
            for language in country['languages']:
                if language not in language_lst:
                    language_lst.append(language)
                    total_languages += 1
                else:
                    continue

print(f'The total number of languages in the data are: {total_languages} languages.')

input(' # Go to the data folder and use the countries_data.py file.\n2. Find the ten most spoken languages from the data')
all_language_lst = []
for country in countries_data:
    for key in country:
        if key == 'languages':
            for language in country['languages']:
                all_language_lst.append(language)


all_language_lst.sort()

# Pending
input(' # Go to the data folder and use the countries_data.py file.\n3. Find the 10 most populated countries in the world')
#Pendig

