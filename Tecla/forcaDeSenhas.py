# Variables

password = input("Escreva a password: ")

rating = 0
rating_length = 0
rating_digit = 0
rating_upper = 0
rating_lower = 0
rating_special = 0

# Validation

while password == "":
    print("Password Inválida")
    password = input("Escreva a password: ")

# Process

for letter in password:
    if len(password) > 8:
        rating_length = 1
    if letter in "1234567890":
        rating_digit = 1
    if letter in "ABCDEFGHIJKLMNOPQRSTUVWXYZÇ":
        rating_upper = 1
    if letter in "abcdefghijklmnopqrstuvwxyzç":
        rating_lower = 1
    if letter in "#&$@%!?;:.-_=+*<>\/^~[](){}":
        rating_special = 1
    # Eficiency
    if rating_length == 1 and rating_digit == 1 and rating_upper == 1 and rating_lower == 1 and rating_special == 1:
        break

rating = rating_length + rating_digit + rating_upper + rating_lower + rating_special

# Output

if rating == 1:
    print("Muito Fraca")
elif rating == 2:
    print("Fraca")
elif rating == 3:
    print("Média")
elif rating == 4:
    print("Forte")
elif rating == 5:
    print("Muito Forte")