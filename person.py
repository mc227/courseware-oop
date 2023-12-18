"""
docstring
"""
class Person:
    """
    docstring
    """
    def __init__(self, first, middle,last):
        self.first = first
        self.middle = middle
        self.last = last
        
    def full_name(self):
        """
        docstring
        """
        return self.first + " " + self.middle + " " + self.last
    def formal_name(self, title):
        """
        docstring
        """
        return title + " " + self.full_name()

if __name__ == "__main__":
    person = Person("Mark", "Christopher", "Costales")
    print(person.formal_name("Mr."))
