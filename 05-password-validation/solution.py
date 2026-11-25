# Case study 29: Password Policy Validation Engine
# These are sample passwords, not real account passwords.

password = input("Enter a sample password: ")
upper = False
lower = False
digit = False
special = False
repeated = False
errors = []

for character in password:
    if "A" <= character <= "Z":
        upper = True
    elif "a" <= character <= "z":
        lower = True
    elif "0" <= character <= "9":
        digit = True
    elif character in "!@#$%":
        special = True

if len(password) < 8:
    errors.append("minimum length is 8")
if not upper:
    errors.append("missing uppercase letter")
if not lower:
    errors.append("missing lowercase letter")
if not digit:
    errors.append("missing digit")
if not special:
    errors.append("missing special character (!@#$%)")

for position in range(len(password) - 2):
    if password[position] == password[position + 1] == password[position + 2]:
        repeated = True
if repeated:
    errors.append("three identical consecutive characters")

for word in ["password", "admin", "123456"]:
    if word in password.lower():
        errors.append("contains prohibited text: " + word)

if errors:
    print("INVALID")
    for error in errors:
        print("-", error)
else:
    print("VALID")
