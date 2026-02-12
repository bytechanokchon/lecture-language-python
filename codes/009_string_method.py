title: str = "String method"
print(f"Techinh content {title}")

full_name: str = input("Enter your full name: ")

print(len(full_name))
print(full_name.find("e"))
print(full_name.rfind("e"))
print(full_name.capitalize())
print(full_name.upper())
print(full_name.lower())
print(full_name.isdigit())
print(full_name.isalpha())
print(full_name.count("e"))
print(full_name.replace("e", "-"))
print(help(str))