import sys

params = sys.argv[1:]

if len(params) == 1:
    z_count = params[0].count("z")
    if z_count == 0:
        print("none")
    else:
        print("z" * z_count)
else:
    print("none")  