# 1. Declare an empty list
empty_list = []
# 2. Declare a list with more than 5 items
twice_members = ['nayeon', 'jeonyeong', 'dahyun', 'chaeyoung', 'jihyo', 'tzuyu', 'momo', 'mina', 'sana']
# 3. Find the length of your list
twice_members_len = len(twice_members)
# 4. Get the first item, the middle item and the last item of the list
first_item_twice = twice_members[0]
middle_item_twice =  twice_members[len(twice_members)//2]
last_item_twice = twice_members[-1]
# 5. Declare a list called mixed_data_types, put your(name, age, height, marital status, address)
mixed_data_types = ['Paula', 23, 1.55, 'single', {'country':'Chile', 'city':'Santiago'}]
# 6. Declare a list variable named it_companies and assign initial values Facebook, Google, Microsoft, Apple, IBM, Oracle and Amazon.
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IMB', 'Oracle', 'Amazon']
# 7. Print the list using print()
print(it_companies)
# 8. Print the number of companies in the list
number_companies = len(it_companies)
print(number_companies)
# 9. Print the first, middle and last company
first_company = it_companies[0]
middle_company =  it_companies[number_companies//2]
last_company = it_companies[-1]
print(f'The first company is {first_company}, the middle is {middle_company} and the last one is {last_company}.')
# 10. Print the list after modifying one of the companies
it_companies[0] = 'HUAWEI'
print(it_companies)
# 11. Add an IT company to it_companies
it_companies.append('Samsung')
# 12. Insert an IT company in the middle of the companies list
it_companies.insert(len(it_companies)//2, 'Intel')
# 13. Change one of the it_companies names to uppercase (IBM excluded!)
it_companies[-3] = 'IBM excluded!'.upper()
# 14. Join the it_companies with a string '#;  '
it_companies_str = '#;  '.join(it_companies)
# 15. Check if a certain company exists in the it_companies list.
amazon_is_company = 'Amazon' in it_companies
# 16. Sort the list using sort() method
it_companies.sort()
# 17. Reverse the list in descending order using reverse() method
it_companies.reverse()
# 18. Slice out the first 3 companies from the list
top_companies = it_companies[0:3]
# 19. Slice out the last 3 companies from the list
last_companies = it_companies[-3:]
# 20. Slice out the middle IT company or companies from the list
middle_company = it_companies[len(it_companies)//2]
# 21. Remove the first IT company from the list
it_companies.pop(0)
# 22. Remove the middle IT company or companies from the list
it_companies.pop(len(it_companies)//2)
# 23. Remove the last IT company from the list
it_companies.pop()
# 24.  Remove all IT companies from the list
it_companies.clear()
# 25. Destroy the IT companies list
del it_companies
# 26. Join the following lists:
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
programming_areas = front_end + back_end
# 27. After joining the lists in question 26. Copy the joined list and assign it to a variable full_stack. Then insert Python and SQL after Redux.
full_stack = programming_areas.copy()
full_stack.insert(-1, 'Python')
full_stack.insert(-1, 'SQL')
full_stack.insert(-1, 'Redux')