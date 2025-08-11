month = "August"

def factorial(n):
    # Base case: factorial of 0 is 1
    if n == 0:
        return 1
    # Recursive case: n * factorial of (n-1)
    else:
        return n * factorial(n - 1)
    
def f1(x):
    return x * x

def f2(m, n):
    m_square = m * m
    n_square = n * n
    sum_square = m_square + n_square
    return sum_square ** 0.5

def sum_to_n(n):
    total = 0
    for number in range(n):
        total = total + number
        # total += number
    return total

# Class definition
class Person:
    # Constructor (initializing attributes)
    def __init__(self, name, age):
        self.name = name   # Attribute: name
        self.age = age     # Attribute: age
    
    # Method to greet
    def greet(self):
        return f"Hello, my namessss is {self.name} and I am {self.age} years old."
    
    def print_age(self):
        print(f"The age is {self.age}")