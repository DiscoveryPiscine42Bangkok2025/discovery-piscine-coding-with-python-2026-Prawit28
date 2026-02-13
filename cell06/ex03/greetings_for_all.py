import sys

def greetings_for_all(name):
    if name is None:
        print("noble stranger")
    elif not isinstance(name, str):
        print("Error! It was not a name")
    else:
        print("Hello, " + name)

greetings_for_all('Alexandra')
greetings_for_all('Wil')
greetings_for_all(None)
greetings_for_all(42)