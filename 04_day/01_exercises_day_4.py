# 1. Concatenate the string 'Thirty', 'Days', 'Of', 'Python' to a single string, 'Thirty Days Of Python'.
espace = ' '
exercise_1  = 'Thirty' + espace + 'Days' + espace + 'Of' + espace + 'Python'

# 2. Concatenate the string 'Coding', 'For' , 'All' to a single string, 'Coding For All'.
exercise_2 = 'Coding' + espace + 'For' + espace + 'All'

# 3. Declare a variable named company and assign it to an initial value "Coding For All".
company = 'Coding For All'

# 4. Print the variable company using print().
print(company)

# 5. Print the length of the company string using len() method and print().
print(len(company))

# 6. Change all the characters to uppercase letters using upper() method.
print(company.upper())

# 7. Change all the characters to lowercase letters using lower() method.
print(company.lower())

# 8. Use capitalize(), title(), swapcase() methods to format the value of the string Coding For All.
print(company.capitalize())
print(company.title())
print(company.swapcase())

# 9. Cut(slice) out the first word of Coding For All string.
print(company[0:6])

# 10. Check if Coding For All string contains a word Coding using the method index, find or other methods.
print(company.index('Coding')) # Give me the position
print(company.find('Coding')) #

# 11. Replace the word coding in the string 'Coding For All' to Python.
print(exercise_1.replace('Coding', 'Singing'))

# 12. Change Python for Everyone to Python for All using the replace method or other methods.
exercise_13 = 'Python for Everyone'
print(exercise_13.replace('Everyone', 'All'))

# 13. Split the string 'Coding For All' using space as the separator (split())
exercise_14 = company.split(' ')
print(exercise_14)

# 14. "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" split the string at the comma.
exercise_15 = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
print(exercise_15.split(',')) 

# 15. What is the character at index 0 in the string Coding For All.
print(company[0])

# 16. What is the last index of the string Coding For All.
print(company[-1])

# 17. What character is at index 10 in "Coding For All" string.
print(company[10])

# 18. Create an acronym or an abbreviation for the name 'Python For Everyone'.
list_PFE = exercise_13.split(' ')

acronym_19 = list_PFE[0][0] + list_PFE[1][0] + list_PFE[2][0]
print('acronym for Python For Everyone: ', acronym_19)

# 19. Create an acronym or an abbreviation for the name 'Coding For All'.
list_CFA = exercise_2.split(' ')

acronym_20 = list_CFA[0][0] + list_CFA[1][0] + list_CFA[2][0]
print('acronym for Coding For All: ', acronym_19)

# 20. Use index to determine the position of the first occurrence of C in Coding For All.
print(company.index('C'))

# 21. Use index to determine the position of the first occurrence of F in Coding For All.
print(company.index('F'))

# 22. Use rfind to determine the position of the last occurrence of l in Coding For All People.
string_23 = 'Coding For All People'
print(string_23.rfind('l'))

# 23. Use index or find to find the position of the first occurrence of the word 'because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
sentence_24 = 'You cannot end a sentence with because because because is a conjunction'
print(sentence_24.find('because'))

# 24. Use rindex to find the position of the last occurrence of the word because in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
sentence_25 = 'You cannot end a sentence with because because because is a conjunction'
print(sentence_25.rindex('because'))

# 25. Slice out the phrase 'because because because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
print(sentence_25[31:-17])

# 26. Find the position of the first occurrence of the word 'because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
print(sentence_25.find('because'))

# 27. Slice out the phrase 'because because because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
sentence_27 = 'You cannot end a sentence with because because because is a conjunction'
print(sentence_27[-40:-17])

# 28. Does ''Coding For All' start with a substring Coding?
print('Coding' in sentence_25[0:5])

# 29. Does 'Coding For All' end with a substring coding?
print('coding' in sentence_25[-6:-1])

# 30. '   Coding For All      '  , remove the left and right trailing spaces in the given string.
sentence_29 = '   Coding For All      '
print(sentence_29.replace('   ', ''))

# 31. Which one of the following variables return True when we use the method isidentifier():
print('30DaysOfPython'.isidentifier())#   30DaysOfPython   False
print('thirty_days_of_python'.isidentifier())#   thirty_days_of_python   True

# 32. The following list contains the names of some of python libraries: ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']. Join the list with a hash with space string.
libraries_python = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
print(' # '.join(libraries_python))

# 33. Use the new line escape sequence to separate the following sentences.
print('I am enjoying this challenge.\nI just wonder what is next.')

# 34. Use a tab escape sequence to write the following lines  .
print('Name\tAge\tCountry\tCity\nAsabeneh\t250\tFinland\tHelsinki')

# 35. Use the string formatting method to display the following:
radius = 10
area = 3.14 * radius ** 2
print(f'The area of a circle with radius {radius} is {area} meters square.')

# 36. Make the following using string formatting methods:
num_8 = 8
num_6 = 6
print(f'{num_8} + {num_6} = {num_8 + num_6}\n{num_8} - {num_6} = {num_8 - num_6}\n{num_8} * {num_6} = {num_8 * num_6}\n{num_8} / {num_6} = {num_8 / num_6:.2f}\n{num_8} % {num_6} = {num_8 % num_6}\n{num_8} // {num_6} = {num_8 // num_6}\n{num_8} ** {num_6} = {num_8 ** num_6}\n')
