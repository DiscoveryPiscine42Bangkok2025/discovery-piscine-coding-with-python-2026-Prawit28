import sys

params = sys.argv[1:]

if len(params) == 2:
    start = int(params[0])
    end = int(params[1])
    print(list(range(start, end + 1)))
else:
    print("none")  