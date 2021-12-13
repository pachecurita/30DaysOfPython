# Exercises: Level 1
input('Exercise 1. Iterate 0 to 10 using for loop, do the same using while loop.')
for i in range(11):
    print(i)
input('While loop:')
count = 0
while count < 11:
    print(count)
    count += 1

input('Exercise 2. # Iterate 10 to 0 using for loop, do the same using while loop.')
for i in range(10, -1, -1):
    print(i)

input('While loop:')
count = 10
while count > -1:
    print(count)
    count -= 1

input('Exercise 3. Write a loop that makes seven calls to print(), so we get on the output the following triangle:')
  #
  ##
  ###
  ####
  #####
  ######
  #######
tag = '#'
addin = ''
for i in range(7):
    addin = addin + tag
    print(addin)

input('Exercise 4. # Use nested loops to create the following:')
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
tag = []
for i in range(8):
    tag += '#'
    if len(tag) == 8:
        for x in tag:
            print(' '.join(tag))


input('Exercise 5. Print the following pattern: ')
# 0 x 0 = 0
# 1 x 1 = 1
# 2 x 2 = 4
# 3 x 3 = 9
# 4 x 4 = 16
# 5 x 5 = 25
# 6 x 6 = 36
# 7 x 7 = 49
# 8 x 8 = 64
# 9 x 9 = 81
# 10 x 10 = 100
for i in range(0, 11):
    print(i, ' x ', i, ' = ', i**2)
    #print(f'{i} x {i} = {i**2}')

input("Exercise 6. # Iterate through the list, ['Python', 'Numpy','Pandas','Django', 'Flask'] using a for loop and print out the items.")

lst = ['Python', 'Numpy','Pandas','Django', 'Flask']
for item in lst:
    print(item)

input('Exercise 7. # Use for loop to iterate from 0 to 100 and print only even numbers')
for i in range(101):
    if i % 2 == 0:
        print(i)

input('Exercise 8. # Use for loop to iterate from 0 to 100 and print only odd numbers')

for i in range(101):
    if i % 2 != 0:
        print(i)
        