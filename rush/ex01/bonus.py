import sys
import os
from checkmate import checkmate

def visual_board(board_str):
    """
    ฟังก์ชัน Creative Bonus: แสดงผลกระดานหมากรุกให้สวยงามและอ่านง่าย
    """
    lines = [line.strip() for line in board_str.strip().split('\n') if line.strip()]
    if not lines:
        return
    
    size = len(lines)
    separator = "+" + "---+" * size
    print(separator)
    for row in lines:
        # แสดงหมากแต่ละตัวในช่องตาราง
        row_display = "| " + " | ".join(row) + " |"
        print(row_display)
        print(separator)

def process_chess_file(filepath):
    """
    ฟังก์ชันสำหรับอ่านไฟล์ .chess และส่งไปตรวจสอบ
    """
    if not os.path.exists(filepath):
        print("Error")
        return

    try:
        with open(filepath, 'r') as file:
            content = file.read()
            if not content.strip():
                print("Error")
                return
            
            # ส่วนเสริม: แสดงชื่อไฟล์และหน้าตากระดาน (Creative Part)
            print(f"\n[ไฟล์: {filepath}]")
            visual_board(content)
            
            # เรียกใช้ Logic หลักจาก checkmate.py
            print("ผลการตรวจสอบ: ", end="")
            checkmate(content)
    except Exception:
        print("Error")

def main():
    """
    รองรับการรับไฟล์หลายไฟล์จาก Arguments (Bonus Option 1)
    """
    # หากไม่มี arguments ให้แสดงวิธีใช้
    if len(sys.argv) < 2:
        print("วิธีใช้งาน: python3 bonus.py [file1.chess] [file2.chess] ...")
        return

    # ประมวลผลทุกไฟล์ที่ระบุในคำสั่ง
    for i in range(1, len(sys.argv)):
        process_chess_file(sys.argv[i])

if __name__ == "__main__":
    main()