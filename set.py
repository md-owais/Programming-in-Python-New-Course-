from os import remove


set_a = {1, 2, 3, 4, 5} # Duplicate values will not allow
# set_a.add(6)
# set_a.remove(2)
# set_a.discard(2) # remove & discard both are same
set_b = {4, 5, 6, 7, 8}

# print(set_a)

# print(set_a.union(set_b))
print(set_a | set_b)
# print(set_a.intersection(set_b))
print(set_a & set_b)

# print(set_a.difference(set_b))
print(set_a - set_b)
print(set_a.symmetric_difference(set_b))
print(set_a ^ set_b)