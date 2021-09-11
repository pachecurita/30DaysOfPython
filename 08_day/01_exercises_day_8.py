# 💻 Exercises: Day 8
# Create an empty dictionary called dog
dog = {}
# Add name, color, breed, legs, age to the dog dictionary
dog = {
    'name':'Bubu',
    'color':'Brown',
    'breed':'Husky',
    'legs':4,
    'age':1
    }
# Create a student dictionary and add first_name, last_name, gender, age, marital status, skills, country, city and address as keys for the dictionary
student = {
    'first_name':'paula',
    'last_name':'diaz',
    'gender':'female',
    'age':23,
    'marital_status':'single',
    'skills':['guitar', 'piano'],
    'country':'chile',
    'city':'santiago',
    'address':{
        'street':'mystreet',
        'zipcode':'000001',
    }, 
}
# Get the length of the student dictionary
student_leng = len(student)
# Get the value of skills and check the data type, it should be a list
student_skills = student['skills']
# Modify the skills values by adding one or two skills
student['skills'] += ['sleep', 'sing']
# Get the dictionary keys as a list
student_keys_lt = student.keys()
# Get the dictionary values as a list
student_values_lt = student.values()
# Change the dictionary to a list of tuples using items() method
student_tuple = student.items()
# Delete one of the items in the dictionary
del student['address']
# Delete one of the dictionaries
del dog