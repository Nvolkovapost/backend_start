def greet():
    name = input("What's your name?").strip()
    while not name:
        name = input("Name can't be empty. Try again.").strip()
    print(f"Nice to meet you, {name}!")


greet()
print("Это мини-практика Git")
