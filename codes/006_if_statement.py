title: str = "If statement"
print(f"Teching content {title}")

age: int = int(input("Enter your age: "))

if age >= 100:
    print("You are to old to sign up")
elif age >= 18:
    print("You are now sign up")
elif age <= 0:
    print("You haven't been born yet!")
else:
    print("You must be 18+ to sigm up")