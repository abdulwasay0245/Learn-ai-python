# Print 10 random numbers in the range 1 to 100 
# .

import random
import time

# Print 10 random numbers in the range 1 to 100 in a line
for i in range(10):
    print(random.randint(1, 100), end=" ")

# Print 10 random numbers in the range 1 to 100 in different lines with a delay of 0.5 seconds
for i in range(10):
    print(random.randint(1, 100))
    time.sleep(0.5)


