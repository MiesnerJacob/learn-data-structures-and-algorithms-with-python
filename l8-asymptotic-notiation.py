import math

def constant_time(n):
    return "Operation in constant time"

def logarithmic_time(n):
    return math.log(n)

def linear_time(n):
    sum = 0
    for i in range(n):
        sum += i
    return sum

def linearithmic_time(n):
    sum = 0
    for i in range(n):
        for j in range(int(math.log(n) + 1)):
            sum += i + j
    return sum

def quadratic_time(n):
    sum = 0
    for i in range(n):
        for j in range(n):
            sum += i + j
    return sum

def exponential_time(n):
    if n == 0:
        return 1
    else:
        return exponential_time(n-1) + exponential_time(n-1)
    
def factorial_time(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial_time(n-1)