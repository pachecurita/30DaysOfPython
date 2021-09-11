A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}

# Exercises: Level 2
# Join A and B
A_union_B = A.union(B)
# Find A intersection B
intersection_AB = A.intersection(B)
# Is A subset of B
A_subset_B = A.issubset(B)
# Are A and B disjoint sets
A_disjoint_B = A.isdisjoint(B)
# Join A with B and B with A
B_union_A = B.union(A)
# What is the symmetric difference between A and B
symetric_diff_AB = A.symmetric_difference(B)
# Delete the sets completely
del A, B