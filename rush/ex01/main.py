import sys
import os
from checkmate import checkmate

def process_chess_file(filepath):
    if not os.path.exists(filepath):
        print("Error from no file in path")
        return

    try:
        with open(filepath, 'r') as file:
            content = file.read()
            if not content.strip():
                print("Error from empty file")
                return
            
            print(f"\n[file: {filepath}]")
            
            print("check result: ", end="")
            print(checkmate(content))
    except Exception:
        print("Error from open file")

def main():
    if len(sys.argv) < 2:
        print("Error no parameters")
        return

    for i in range(1, len(sys.argv)):
        process_chess_file(sys.argv[i])

if __name__ == "__main__":
    main()