import math

a: float = float(input("Enter side A: "))
b: float = float(input("Enter side B: "))

c: float = math.sqrt(pow(a, 2) + pow(b, 2))

print(f"Side C = {c}")