print("Teching content For loop")

print("normal loop")
for x in range(1, 10):
    print(x)

# กลับด้านข้อมูลใน range
print("reserve loop")
for x in reversed(range(0,10)):
    print(x)

# การใช้งาน range แบบระบุ step
print("range with step")
for x in range(0, 10, 2):
    print(x)

# การใช้งาน for ร่วมกับ string
print("loop string")
credit_card: str = "1234-5678-9012-3456"
for x in credit_card:
    print(x)