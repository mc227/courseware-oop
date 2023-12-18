"""
mark.py
"""

def new_person(first,last):
    """
    docstring
    """
    return {"first": first, "last": last}


def full_name(person):
    """
    docstring
    """
    return person["first"] + " " + person["last"]

def formal_name(person, title):
    """
    docstring
    """
    return title + " " + full_name(person
    )
if __name__ == "__main__":
    print("oh hi Mark")
