
'''
# Method-1
file = open('test.txt', mode = 'r')

data = file.readline()

print(data)
file.close()
'''

# Method-2
with open('test.txt', mode = 'r') as file:
    data = file.readline()
    print(data)
