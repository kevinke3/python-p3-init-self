#!/usr/bin/env python3

class Dog:
    def __init__(self,name, breed = 'mutt') :
        self.name = name
        self.breed = breed
bosco = Dog('Bosco','german')
print(bosco.breed)