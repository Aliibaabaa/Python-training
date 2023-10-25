'''
def greet(name):
    print("Hello,", name + "!")

greet("Sample_name")
'''

def greet(name):
    return "hello "+name 

# print(greet("sample_name"))

# greet = greet("sample_name")
# print(greet)

#####

import math
print(math.sqrt(16)) #Output : 4.0

####

class Person:
    def __init__(self, name):
        self.name = name
    
    def greet(self):
        return f"Hello, my name is {self.name}"
    
person = Person("Alice")
print(person.greet()) # Output: Hello, my name is Alice


