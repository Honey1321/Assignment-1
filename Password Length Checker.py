password = input("Enter a password: ")
has_upper = False
has_lower = False
has_digit = False
for ch in password:
    if ch.isupper():
        has_upper = True
    elif ch.islower():
        has_lower = True
    elif ch.isdigit():
        has_digit = True
    else:
        pass
if (
    len(password) >= 8
    and has_upper
    and has_lower
    and has_digit
):
    print("Password meets the basic strength rules")
else:
    print("Password is weak. Use 8+ characters with uppercase, lowercase and digits.")
