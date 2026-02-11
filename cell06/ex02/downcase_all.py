import sys

def downcase_it(str):
    return str.lower()

params = sys.argv[1:]

if len(params) > 0:
    for i in params:
        print(downcase_it(i))
else:
    print("none")
