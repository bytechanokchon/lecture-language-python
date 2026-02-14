title: str = "String Indexing"
print(f"Teching content {title}")

credit_number: str = "1234-5678-9012-3456"

print(f"{credit_number[0]}")
print(f"{credit_number[0:4]}")

# ตั้งแต่ตำแหน่งแรกไปจนถึงตำแหน่งที่ระบุ
print(f"{credit_number[:4]}") 

# ตั้งแต่ index ที่ 5 ไปจนถึงตำแหน่งสุดท้าย
print(f"{credit_number[5:]}") 

# เข้าถึงตำแหน่งสุดท้าย (ยิ่งจำนวนลบเยอะ ก็ยิ่งถอยตำแหน่งที่จะเข้าถึงมาเรื่อย ๆ)
print(f"{credit_number[-1]}") 

# เข้าถึงข้อมูลใน string โดยขยับไปเรื่อย ๆ ทุก ๆ 2 ตำแหน่ง
print(f"{credit_number[::2]}")

# เข้าถึง 4 ตำแหน่งสุดท้าย
print(f"{credit_number[-4:]}")

# เข้าถึงข้อมูลใน string โดยขยับถอยหลังทีละ 1 (ทำให้ข้อมูลย้อนกลับ)
print(f"{credit_number[::-1]}")