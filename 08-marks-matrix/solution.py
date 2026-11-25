# Case study 42: Student Marks Matrix Analysis
# Each row is a student and each column is a subject.

subjects = ["Maths", "Physics", "Python"]
count_text = input("Number of students (1 to 20): ").strip()
if not count_text.isdecimal() or not 1 <= int(count_text) <= 20:
    print("Enter a number from 1 to 20.")
else:
    names = []
    matrix = []
    for number in range(int(count_text)):
        print("\nStudent", number + 1)
        name = input("Name: ").strip()
        parts = input("Marks in Maths, Physics and Python: ").split()
        row = []
        valid = bool(name) and len(parts) == 3
        if valid:
            for part in parts:
                if not part.isdecimal() or int(part) > 100:
                    valid = False
                    break
                row.append(int(part))
        if valid:
            names.append(name)
            matrix.append(row)
        else:
            print("Invalid record: enter a name and 3 marks from 0 to 100.")

    if not matrix:
        print("\nNo valid student records.")
    else:
        print("\nStudent totals and averages:")
        highest_total = -1
        for row in range(len(matrix)):
            total = sum(matrix[row])
            average = total / len(subjects)
            print(f"{names[row]}: total {total}, average {average:.2f}")
            if total > highest_total:
                highest_total = total
        print("Top performer(s):")
        for row in range(len(matrix)):
            if sum(matrix[row]) == highest_total:
                print(names[row], "- total", highest_total)

        print("\nSubject averages:")
        for column in range(len(subjects)):
            total = 0
            for row in range(len(matrix)):
                total += matrix[row][column]
            average = total / len(matrix)
            if average < 60:
                print(f"{subjects[column]}: {average:.2f} - low average")
            else:
                print(f"{subjects[column]}: {average:.2f}")
