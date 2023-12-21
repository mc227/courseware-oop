"""
animals.py
"""
class Dog:
    """
    Dog
    """
    def __init__(self, name):
        self.name = name
    def describe(self):
        """
        describe
        """
        return 'the dog says: Woof!'

class Bird:
    """
    Bird
    """
    def __init__(self, name):
        self.name = name
    def describe(self):
        """
        describe
        """
        return 'the bird says: Chirp!'

class Cat:
    """
    Cat
    """
    def __init__(self, name):
        self.name = name
    def describe(self):
        """
        describe
        """
        return 'the cat says: Meow!'

if __name__ == "__main__":
    fido = Dog("Fido")
    print(fido.describe())
