print("Teching content: Nested Loop")

rows: int = int(input("Enter the # of rows: "))
cols: int = int(input("Enter the # of cols: "))
symbol: str = input("Enter the symbol to use: ")

for count in range(rows):
    for x in range(cols):
        # การตั้งค่า end คือการระบุว่าตัวสุดท้ายของ string จะให้ลงท้ายด้วยอะไร
        # โดยค่าเริ่มต้นคือ \n
        print(symbol, end=" ")
    print()

