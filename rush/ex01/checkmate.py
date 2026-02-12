def checkmate(board_str):
    if not board_str or not board_str.strip():
        return

    # Split board into lines and filter out empty strings
    lines = [line for line in board_str.strip().split('\n') if line]
    size = len(lines)
    
    # Validation: Board must be square
    for line in lines:
        if len(line) != size:
            return

    # Find King's position (row, col)
    k_pos = None
    for r in range(size):
        for c in range(size):
            if lines[r][c] == 'K':
                k_pos = (r, c)
                break
        if k_pos:
            break
            
    if not k_pos:
        return

    kr, kc = k_pos

    # Directions: (row_delta, col_delta)
    # Straight: Up, Down, Left, Right
    straight = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    # Diagonal: Up-Left, Up-Right, Down-Left, Down-Right
    diagonal = [(-1, -1), (-1, 1), (1, -1), (1, 1)]

    # 1. Check for Rooks (R) and Queens (Q) in straight lines
    for dr, dc in straight:
        r, c = kr + dr, kc + dc
        while 0 <= r < size and 0 <= c < size:
            piece = lines[r][c]
            if piece == 'R' or piece == 'Q':
                print("Success")
                return
            elif piece != '.': # Blocked by another piece
                break
            r += dr
            c += dc

    # 2. Check for Bishops (B) and Queens (Q) in diagonal lines
    for dr, dc in diagonal:
        r, c = kr + dr, kc + dc
        while 0 <= r < size and 0 <= c < size:
            piece = lines[r][c]
            if piece == 'B' or piece == 'Q':
                print("Success")
                return
            elif piece != '.': # Blocked by another piece
                break
            r += dr
            c += dc

    # 3. Check for Pawns (P)
    # Note: In the subject's diagram, Pawns attack from "above" relative to the board layout
    # Assuming the board is oriented with enemy Pawns moving from top to bottom (row+1)
    # or bottom to top (row-1). Usually, in these subjects, 'P' captures from diagonal rows.
    # We check the two diagonals immediately above the King.
    pawn_check_positions = [(kr - 1, kc - 1), (kr - 1, kc + 1)]
    for pr, pc in pawn_check_positions:
        if 0 <= pr < size and 0 <= pc < size:
            if lines[pr][pc] == 'P':
                print("Success")
                return

    # If no piece is found
    print("Fail")