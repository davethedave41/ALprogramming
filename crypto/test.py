import sys
import json
import io

class Person:
    age = 23
    name = "Adam"

jahoo = {
            'username': 'davethedave',
            'job': 'cuck',
            'age': 21,
            'wah': []
        }
print(jahoo['wah'])
jahoo['wah'].append(2)
print(jahoo['wah'])
