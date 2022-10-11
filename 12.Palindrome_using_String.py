str = input("Enter the string:")
str = str.casefold()
if(str==str[::-1]):
    print("Palindrome")
else:
    print("Not palindrome")