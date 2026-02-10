import sys

if len(sys.argv) - 1 == 1:
    keyword = sys.argv[1]
    string = input("What was the parameter? ")
    if keyword in string:
        print("Good job!")
    else:
        print("Nope, sorry...")
else:
    print("none")  