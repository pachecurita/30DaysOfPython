# Exercises: Level 3

from countries import countries
from countries_data import countries_data

input('# I. Go to the data folder and use the countries.py file. Loop through the countries and extract all the countries containing the word land.')

for country in countries:
    if 'land' in country:
        print(country)

input("\n# II. This is a fruit list, ['banana', 'orange', 'mango', 'lemon'] reverse the order using loop.")

fruit_list = ['banana', 'orange', 'mango', 'lemon']
fruit_list_reversed = []

for i in fruit_list:
    fruit_list_reversed.insert(0, i)

print(fruit_list_reversed)

input(' \n# III. Go to the data folder and use the countries_data.py file.\n1. What are the total number of languages in the data')
language_lst = []
for data_country in countries_data:
    for key in data_country:
        if key == 'languages':
            for language in data_country['languages']:
                if language not in language_lst:
                    language_lst.append(language)

                else:
                    continue

language_lst.sort()
print(f'The total number of languages in the data are: {len(language_lst)} languages.')

input(' \n2. Find the ten most spoken languages from the data')
list_of_all_countries_repeated = []
for data_country in countries_data:
    for language in data_country['languages']:
        list_of_all_countries_repeated.append(language)

list_of_all_countries_repeated.sort()

list_of_times_appears = []
for i in language_lst:
    count = 0
    for j in list_of_all_countries_repeated:
        if i == j:
            count += 1
    list_of_times_appears.append(count)

new_list = []
for i in range(len(language_lst)):
    new_list += [[language_lst[i], list_of_times_appears[i]]]

for i in range(12):
    top_times = 0
    top_country = ''
    for element in new_list:
        if element[1] > top_times:
            top_times = element[1]
            top_country = element[0]
            index = new_list.index(element)
    print(f'{i+1}.- {top_country} is spoken in {top_times} countries.')
    new_list.pop(index)

input(' \n3. Find the 10 most populated countries in the world')
for i in range(11):
    popu_country = ''
    popu = 0
    for country in countries_data:
        if country['population'] > popu:
            popu = country['population']
            popu_country = country['name']
            inde = countries_data.index(country)
    print(f'{i+1}.- {popu_country} with a {popu} population.')
    countries_data.pop(inde)
