import sys

class Person:
    age = 23
    name = "Adam"

person = Person()
print(str(getattr(person, "name")))
print(sys.modules['__main__'])
