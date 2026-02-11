import sys

def shrink(str):
    return str[:8]

def enlarge(str):
    while len(str) < 8:
        str += "z"
    return str

def main():
    if len(sys.argv)-1 != 0:
        for i in range(1, len(sys.argv)):
            if len(sys.argv[i]) < 8:
                print(enlarge(sys.argv[i]))
            else:
                print(shrink(sys.argv[i]))
    else:
        print("None")

if __name__ == "__main__":
    main()