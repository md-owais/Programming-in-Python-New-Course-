my_d = {1: ' Test', 'Name': 'Jim', 1: 'Not a test'}
# Dictionary does not allow duplicate values

# print(type(my_d))
# my_d[2] = 'Test 2'
# print(my_d[1])

# my_d[1] = 'Not a test!'
# del my_d[1]

# for x in my_d: # This will give only keys
#     print(x)
# print(my_d)

for key, value in my_d.items():
    print(str(key) + ":" + value)