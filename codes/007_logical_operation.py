title: str = "Logical Operation"
print(f"Teching content {title}")

temp: int = 25
is_raining: bool = False

is_hot: bool = temp > 35
is_cool: bool = temp < 0

if is_hot or is_cool or is_raining:
    print("The outdoor event is cancelled")
else:
    print("The outdoor event is still scheduled")

is_sunny: bool = True
if temp < 35 and is_sunny:
    print("It is warm outside")
    print("It is Sunny")