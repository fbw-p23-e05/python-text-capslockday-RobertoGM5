user_input = input("Enter string: ")

if user_input.isupper():
    normalize = user_input.lower() + "!"
else:
    normalize = user_input.lower()

print(normalize.capitalize())