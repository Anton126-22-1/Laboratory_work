def greet(name="світ"):
    return f"Привіт, {name}!"

user_name = input("Введіть своє ім'я: ").strip()
if not user_name:
    message = greet()
else:
    message = greet(user_name)

print(message)
