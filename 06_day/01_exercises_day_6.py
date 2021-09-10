# Exercises: Level 1
# Create an empty tuple
empty_tuple = ()
# Create a tuple containing names of your sisters and your brothers (imaginary siblings are fine)
my_sisters = ('Aylin',)
my_brothers = ('Jose',)
# Join brothers and sisters tuples and assign it to siblings
my_siblings = my_sisters + my_brothers
print(my_siblings)
# How many siblings do you have?
number_siblings = len(my_siblings)
print('I have: ', number_siblings, ' siblings.')
# Modify the siblings tuple and add the name of your father and mother and assign it to family_members
my_parents = ('Ana', 'Jose Manuel')
family_members = my_siblings + my_parents
print('My family names are: ', family_members)

# Exercises: Level 2
# Unpack siblings and parents from family_members
sister, brother, mom, dad = family_members
siblings = sister + ' ' +brother
parents = mom + ' ' + dad
print('Siblings: ', siblings, '\nParents: ', parents)
# Create fruits, vegetables and animal products tuples. Join the three tuples and assign it to a variable called food_stuff_tp.
fruits = ('Orange', 'Apple', 'Watermelon', 'Strawberries')
vegetables = ('Letucce', 'Tomato', 'Avocado')
animal_products = ('Milk', 'Yogurth', 'Cheese', 'Meat')
food_stuff_tp = fruits + vegetables + animal_products
# Change the about food_stuff_tp tuple to a food_stuff_lt list
food_stuff_lt = list(food_stuff_tp)
# Slice out the middle item or items from the food_stuff_tp tuple or food_stuff_lt list.
middle_item_food = food_stuff_tp[len(food_stuff_tp)//2]
# Slice out the first three items and the last three items from food_staff_lt list
first_three = food_stuff_tp[0:3]
last_three = food_stuff_tp[-3:]
# Delete the food_staff_tp tuple completely
del food_stuff_tp

