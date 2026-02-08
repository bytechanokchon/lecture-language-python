item: str = input("What's item would you like to buy ?: ")
price: float = float(input("What is the price ? : "))
quantity: int = int(input("How many would you like ?: "))
total: float = price * quantity

print(f"You have bought {quantity} x {item}/s")
print(f"You total is ${total}")