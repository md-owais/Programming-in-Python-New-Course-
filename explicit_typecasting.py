# Using explicit type conversion, change the following 
# inputs so the types match with the following below
#  
# name = type string
# age = type int
# height = type float
# loyalty = type boolean

# Modify the line below
name = str(input('What is the first name?: '))

print("I am" + str(name))

# Modify the line below
age = int(input('What is your age?: '))

print("I am " + str(age) + " years old")

# Modify the line below
height =float(input('What is your height in meters?: '))

print("I am " + str(height) + " m tall")

# Modify the line below
loyalty =bool(input('Are you part of our loyalty program?: '))
 
print("Yes, I am the part of" + str(loyalty))