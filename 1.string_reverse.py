from audioop import reverse
from tracemalloc import start


# str[start:stop:step]
'''
# Using slice method

trial = "reversal"
new_trial = trial[::-1]
print(new_trial)

'''
# using recursion method
def string_reverse(str):
    if len(str) == 0:
        return str
    else:
        return string_reverse(str[1:]) + str[0]

str = "reversal"
reverse = string_reverse(str)
print(reverse)

