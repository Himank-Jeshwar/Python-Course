import time
# Formula : timeInSec%2 --> Generates a random number b/w 0 and 1
# maximum is excluded

timeInSec = time.time()
randVal = timeInSec%2

print(int(randVal*(125-100)+100))