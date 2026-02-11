import sys

def greetings_for_all(name):
    if name is None:
        return "noble stranger"
    elif name is not str:
        return "Error! It was not a name"
    else:
        return "Hello, " + name

