from checkmate import checkmate

def main():
    board = """\
R...
.K..
..P.
....\
"""
    print(checkmate(board)) 

    board = """\
..
.K\
"""
    print(checkmate(board)) 

if __name__ == "__main__":
    main()