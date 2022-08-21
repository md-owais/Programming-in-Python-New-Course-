
'''
def divide_by(a, b):
    return a / b

try:
    ans: divide_by(40, 0)
except Exception as e:

# print(divide_by(40, 4))
    # print(divide_by(40, 0)) # This will give error

    print("Something went wrong!", e)
    print(e.__class__)

'''
'''
def divide_by(a, b):
    return a / b

try:
    ans: divide_by(40, 0)
except ZeroDivisionError as e:

# print(divide_by(40, 4))
    # print(divide_by(40, 0)) # This will give error

    print(e, "We cannot divide by zero")
    # print(e.__class__)

'''
# How to handle multiple exceptions
def divide_by(a, b):
    return a / b

try:
    ans: divide_by(40, 0)
except ZeroDivisionError as e:

# print(divide_by(40, 4))
    # print(divide_by(40, 0)) # This will give error

    print(e, "We cannot divide by zero")
except Exception as e:
    print(e, "Something went wrong!")
   

