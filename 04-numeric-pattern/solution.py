# Case study 27: Advanced Numeric Pattern Generator
# Print a hollow numeric diamond of an odd height.

size_text = input("Enter an odd height from 3 to 9: ").strip()
if not size_text.isdecimal():
    print("Invalid height: use an odd whole number from 3 to 9.")
else:
    size = int(size_text)
    if size < 3 or size > 9 or size % 2 == 0:
        print("Invalid height: use an odd whole number from 3 to 9.")
    else:
        middle = size // 2
        for row in range(size):
            level = middle - abs(row - middle)
            digit = str(level + 1)
            spaces = middle - level
            if level == 0:
                print(" " * spaces + digit)
            else:
                print(" " * spaces + digit + " " * (2 * level - 1) + digit)
