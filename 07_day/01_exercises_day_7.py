# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}

# Exercises: Level 1
# Find the length of the set it_companies
it_companies_lenght = len(it_companies)
# Add 'Twitter' to it_companies
it_companies.add('Twitter')
# Insert multiple IT companies at once to the set it_companies
it_companies.update(['Samsung', 'HUAWEI'])
# Remove one of the companies from the set it_companies
it_companies.remove('Facebook')
# What is the difference between remove and discard
# The first one can raise errors if doesnt found the element while the other doesnt. Example:
it_companies.discard('Facebook')
#it_companies.remove('Facebook') # Raise a KeyError