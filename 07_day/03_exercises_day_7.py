age = [22, 19, 24, 25, 26, 24, 25, 24]

# Exercises: Level 3
# Convert the ages to a set and compare the length of the list and the set, which one is bigger?
age_st = set(age)
age_st_lenght = len(age_st)
age_lt_lenght = len(age)
compare_age_st_lt = age_st_lenght == age_lt_lenght
# Explain the difference between the following data types: string, list, tuple and set
# String = is a character data type, modifiable.
# List = is a sorted, modifiable list.
# Tuple = is not modifiable, but it is sorted.
# Set = is a list type with a unique elements.
# I am a teacher and I love to inspire and teach people. How many unique words have been used in the sentence? Use the split methods and set to get the unique words.
sentence = 'I am a teacher and I love to inspire and teach people'
print(f'Sentence: {sentence}')
sentence_list = sentence.split(' ')
sentence_set = set(sentence_list)
print(f'There are {len(sentence_set)} unique words used in the sentence: {" , ".join(list(sentence_set))}.')