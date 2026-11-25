# Case study 26: Nested Loop Examination Seating Generator
# The classroom has 4 rows and 5 columns.

reserved = [(1, 1), (2, 3)]
count_text = input("Number of students: ").strip()
if not count_text.isdecimal():
    print("Enter a non-negative whole number.")
else:
    requested = int(count_text)
    assigned = 0
    available = 0
    reserved_count = 0
    blocked = 0
    print("\n     C1   C2   C3   C4   C5")
    for row in range(1, 5):
        line = f"R{row} "
        for column in range(1, 6):
            if (row, column) in reserved:
                seat = "R"
                reserved_count += 1
            elif (row + column) % 2 == 1:
                seat = "X"
                blocked += 1
            else:
                available += 1
                if assigned < requested:
                    assigned += 1
                    seat = f"S{assigned:02d}"
                else:
                    seat = "O"
            line += seat.rjust(5)
        print(line)
    print("R = reserved, X = blocked, O = available")
    print(f"Positions: 20 | Reserved: {reserved_count} | Blocked: {blocked}")
    print(f"Available student seats: {available}")
    print(f"Assigned: {assigned} | Unseated: {requested - assigned}")
