from checkmate import checkmate

def main():
    # Example 1: Rook checking King
    board1 = """
R...
.K..
....
....
"""
    # Example 2: King not in check
    board2 = """
..
K.
"""
    
    # We wrap in try/except to ensure the program never crashes as per instructions
    try:
        checkmate(board1)
        # checkmate(board2)
    except Exception:
        pass

if __name__ == "__main__":
    main()