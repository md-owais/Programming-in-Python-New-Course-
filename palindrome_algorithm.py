# Algorithm for a palindrome
from tracemalloc import start


def isPalindrome(str):
    startIndex = 0
    endIndex = len(str) - 1

    for x in str:
        if str[startIndex] != str[endIndex]:
            return False
    return True
print(isPalindrome('racecar'))