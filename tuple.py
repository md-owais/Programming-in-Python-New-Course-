my_tuple = (1, 'strings', 4.5, True)
print(my_tuple[1])
print(type(my_tuple))
print(my_tuple.count('strings'))
print(my_tuple.index(4.5))
# my_tuple[0] = 5 # It will throw the error
for x in my_tuple:
    print(x)