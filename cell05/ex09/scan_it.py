import sys

if len(sys.argv) - 1 == 2:
    keyword = sys.argv[1]
    string = sys.argv[2]
    if keyword in string:
        print(string.count(keyword))
    else:
        print("none")
else:
    print("none")  