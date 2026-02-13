def checkmate(board_str):
    # 1. ตรวจสอบความถูกต้องของกระดาน (Error Handling)
    if not board_str or not board_str.strip():
        return "Error"

    # แยกบรรทัดและกำจัดช่องว่าง
    lines = [line.strip() for line in board_str.strip().split('\n') if line.strip()]
    
    if not lines:
        return "Error"

    size = len(lines)
    
    # ตรวจสอบว่าเป็นสี่เหลี่ยมจัตุรัสหรือไม่
    for line in lines:
        if len(line) != size:
            return "Error"

    # 2. ค้นหาตำแหน่ง King
    k_pos = None
    for r in range(size):
        for c in range(size):
            if lines[r][c] == 'K':
                if k_pos:
                    return "Error"
                k_pos = (r, c)
            
    if not k_pos:
        return "Error"

    kr, kc = k_pos

    # ฟังก์ชันช่วยเช็คทิศทาง (Ray Casting) สำหรับ R, B, Q
    def check_direction(dr, dc, valid_pieces):
        r, c = kr + dr, kc + dc
        while 0 <= r < size and 0 <= c < size:
            piece = lines[r][c]
            if piece != '.':
                # ถ้าเจอชิ้นส่วน ตรวจสอบว่าเป็นศัตรูที่กินเราได้หรือไม่
                if piece in valid_pieces:
                    return True
                return False # โดนบัง (Blocked)
            r += dr
            c += dc
        return False

    # ตรวจสอบแนวตรง (Rook, Queen)
    straight = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    for dr, dc in straight:
        if check_direction(dr, dc, {'R', 'Q'}):
            return "Success"

    # ตรวจสอบแนวทแยง (Bishop, Queen)
    diagonal = [(-1, -1), (-1, 1), (1, -1), (1, 1)]
    for dr, dc in diagonal:
        if check_direction(dr, dc, {'B', 'Q'}):
            return "Success"

    # 3. ตรวจสอบ Pawn (P)
    # Pawn โจมตีทแยงขึ้นด้านบน (Row - 1)
    # ดังนั้นถ้าเรายืนที่ King เราต้องมองหา Pawn ที่มาจากแถวด้านล่าง (Row + 1)
    # เช็คตำแหน่งล่างซ้าย (kr+1, kc-1) และ ล่างขวา (kr+1, kc+1)
    pawn_check_positions = [(kr + 1, kc - 1), (kr + 1, kc + 1)]
    
    for pr, pc in pawn_check_positions:
        if 0 <= pr < size and 0 <= pc < size:
            if lines[pr][pc] == 'P':
                return "Success"

    # ถ้าไม่เจอการรุกใดๆ เลย
    return "Fail"