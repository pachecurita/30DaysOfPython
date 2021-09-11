# Exercises: Level 3
# Here we have a person dictionary. Feel free to modify it!
person = {
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_married': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
        }
    }

#  * Check if the person dictionary has skills key, if so print out the middle skill in the skills list.
if 'skills' in person:
    skills_person = person['skills']
    print(skills_person[len(skills_person)//2])

#  * Check if the person dictionary has skills key, if so check if the person has 'Python' skill and print out the result.
if 'skills' in person:
    if 'Python' in person['skills']:
        print('The person have Python skills.')
#  * If a person skills has only JavaScript and React, print('He is a front end developer'), if the person skills has Node, Python, MongoDB, print('He is a backend developer'), if the person skills has React, Node and MongoDB, Print('He is a fullstack developer'), else print('unknown title') - for more accurate results more conditions can be nested!
if 'React' in person['skills'] and 'Node' in person['skills'] and 'MongoDB' in person['skills']:
    print('The person is a fullstack developer.')
elif 'JavaScript' in person['skills'] and 'React' in person['skills']:
    print('The person is a frontend developer.')
elif 'Node' in person['skills'] and 'Python' in person['skills'] and 'MongoDB' in person['skills']:
    print('The person is a backend developer.')
else:
    print('Unknown title')
#  * If the person is married and if he lives in Finland, print the information in the following format:
#     Asabeneh Yetayeh lives in Finland. He is married.
if person['is_married'] == True:
    if person['country'] == 'Finland':
        print(person['first_name'], ' lives in ', person['country'], '. He is married.')
