# Case study 1: University Scholarship Allocation
# Each applicant has three marks out of 100.

count_text = input("Number of applicants: ").strip()
if not count_text.isdecimal() or int(count_text) < 1:
    print("Enter a positive number of applicants.")
else:
    eligible = []
    seen_rolls = []
    rejected = 0

    for number in range(int(count_text)):
        print("\nApplicant", number + 1)
        roll = input("Roll number: ").strip().upper()
        name = input("Name: ").strip()
        mark_text = input("Marks in 3 subjects: ").split()
        attendance_text = input("Attendance percentage: ").strip()
        income_text = input("Annual family income: ").strip()
        errors = []
        marks = []

        if not roll or not name:
            errors.append("roll and name are required")
        if roll in seen_rolls:
            errors.append("duplicate roll number")
        if len(mark_text) != 3:
            errors.append("enter exactly 3 marks")
        else:
            for value in mark_text:
                if not value.isdecimal() or int(value) > 100:
                    errors.append("marks must be whole numbers from 0 to 100")
                    break
                marks.append(int(value))
        if not attendance_text.isdecimal() or int(attendance_text) > 100:
            errors.append("attendance must be from 0 to 100")
        if not income_text.isdecimal():
            errors.append("income must be a non-negative whole number")

        if errors:
            print("Invalid record:", "; ".join(errors))
            rejected += 1
            continue

        seen_rolls.append(roll)
        attendance = int(attendance_text)
        income = int(income_text)
        total = sum(marks)
        reasons = []
        if total / 3 < 60:
            reasons.append("aggregate below 60")
        if min(marks) < 50:
            reasons.append("a subject is below 50")
        if attendance < 75:
            reasons.append("attendance below 75")
        if income > 500000:
            reasons.append("income above 500000")

        if reasons:
            print(roll, "not eligible:", "; ".join(reasons))
            rejected += 1
        else:
            # Negative values arrange the higher total and attendance first.
            eligible.append((-total, -attendance, income, roll, name))

    eligible.sort()
    print("\nEligible applicants (ranked):")
    if not eligible:
        print("None")
    for index in range(len(eligible)):
        negative_total, negative_attendance, income, roll, name = eligible[index]
        average = -negative_total / 3
        print(f"{index + 1}. {roll} {name} | average {average:.2f} | "
              f"attendance {-negative_attendance}% | income Rs {income}")
    print(f"Eligible: {len(eligible)} | Rejected or invalid: {rejected}")
