import sys
params = sys.argv[1:]
if len(params) > 1:
    print(f"parameters: {len(params)}")
    for i in params:
        print(f"{i}: {len(i)}")
else:
    print("none")  