# string
first_name = "Chanokchon"
last_name = "Wongjumpa"
food = "pizza"
email = "byte.chanokchon@gmail.com"

# f-string ย่อมาจาก format string ใช้สำหรับ ใช้สำหรับจัดรูปแบบของข้อมูลที่เป็น string
print(f"Hello {first_name} {last_name}\nYou like a {food}\nYour email is {email}")

# integer
age = 25
quantity = 3.5
num_of_student = 30
print(f"You are {age} year old\nYou are buying {quantity} items\nYou class have {num_of_student} students")

# Float
price = 10.99
gpa = 3.4
distance = 5.5
print(f"The price is ${price}\nYour GPA is {gpa}\nYou ran {distance} km")

# Boolean
is_student = True
is_for_sale = True
if is_student:
    print("You are a student")
else:
    print("You are not a student")

if is_for_sale:
    print("That item is for sale")
else:
    print("That item is not avaliable")