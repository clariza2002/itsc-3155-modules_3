import time
import random

def fibonacci(x):
    if(x<=0):
        return 0
    elif(x == 1):
        return 1
    elif(x == 2):
        return 1
    return fibonacci(x-1)+fibonacci(x-2)
x = random.randint(15,35)
start = time.time()
result = fibonacci(x)
end = time.time()
print(f"fib({x})= {result}")
print(f"fib({x})= {end - start}")