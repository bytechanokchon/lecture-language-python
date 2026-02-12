username: str = input("Enter a username : ")

is_valid_length: bool = len(username) <= 12
is_not_contain_space: bool = username.find(" ") == -1
is_contain_only_alpha:bool = username.isalpha()

if not is_valid_length:
    print("Your username can't be more than 12 character")
elif not is_not_contain_space:
    print("Your username can't contain space")
elif not is_contain_only_alpha:
    print("Your username can't contain number")
else:
    print(f"Welcome {username} to Pixer System")