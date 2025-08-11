# Create a module called test_module
# In this module, create a class called Student
# Class Student should have two attributes
    # attribute name 
    # attribute year
# Class Student should define two methods:
    # greet() which should print the student's name and year
    # print_year() which should print the student's year

class Student:
    def __init__(self, name, year):
        self.name = name
        self.year = year
        self.year_square = year * year
        self.school = "Regina"
    
    def greet(self):
        print(f"My name is {self.name}, I am in year {self.year}")

    def print_year(self):
        print(f"My year is {self.year}")

    def print_school(self):
        print(f"My school is {self.school}")


def factorial(n):
    # Base case: factorial of 0 is 1
    if n == 0:
        return 1
    # Recursive case: n * factorial of (n-1)
    else:
        return n * factorial(n - 1)