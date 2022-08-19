from time import time


import time
from tracemalloc import start
start_time = time.time()


# outer loop
# for i in range(10):
# for i in range(1):
for i in range(100):
    #inner loop
    for j in range(100):
        print(0, end = " ")
    print()
print(round((time.time() - start_time), 2))