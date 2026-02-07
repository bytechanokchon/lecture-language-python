name = "Byte Chanokchon"
age = 25
gpa = 2.99
is_student = True 

# type ใช้สำหรับดูว่าตัวแปรกำลังจัดเก็บข้อมูลชนิดอะไรอยู่
print(type(name))
print(type(age))
print(type(gpa))
print(type(is_student))

# แปรง float เป็น int
gpa = int(gpa)
print(gpa)

# แปรง int เป็น float
age = float(age)
print(age)

# แปรง int เป็น string
age = str(age)
print(age)
print(type(age))

# แปรง string เป็น boolean (อยาก string มีค่าจะเป็นจริง นอกนั้นเป็นเท็จ)
comment = "Hello"
print(bool(comment))