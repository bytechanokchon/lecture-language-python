title: str = "Format Specifiers"
print(f"Teching content {title}")

number: float = 1000000.12345

# :number
print("Space with Float")
print(f"Number: {number:<20}")
print(f"Number: {number:>20}")
print(f"Number: {number:^20}")
print("\n")

print("Specific decimal")
print(f"Number: {number:.2f}")
print("\n")

print("Add comma")
print(f"Number: {number:,}")
print("\n")

print("Example")
print(f"Number: {number:+,.2f}")