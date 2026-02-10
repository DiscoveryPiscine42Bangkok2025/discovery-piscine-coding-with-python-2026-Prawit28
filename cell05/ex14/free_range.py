import sys

params = sys.argv[1:]

if len(params) == 2:
    start = int(params[0])
    end = int(params[1])
    arr = []
    for i in range(start, end + 1):
        arr.append(i)
    print(arr)
else:
    print("none")  