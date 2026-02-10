import sys

params = sys.argv[1:]

if len(params) > 0:
    for i in params:
        if not i.endswith("ism"):
            print(i+"ism")
else:
    print("none")  