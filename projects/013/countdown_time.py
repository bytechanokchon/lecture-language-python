import time
print("Countdown timer")

my_time: int = int(input("Enter the time in seconds: "))

for x in reversed(range(0, my_time)):
    print(f"Second: {x + 1}")
    time.sleep(1)

# โปรแกรมหยุดทำงาน 3 วินาที

print("Time's Up!")
