# Case study 64: Tuple-Based Course Registration Validation

known_courses = ("CS101", "CS201", "CS301", "MATH101", "PHY101", "PHY102", "ENG101")
count_text = input("Number of students: ").strip()
if not count_text.isdecimal() or int(count_text) < 1:
    print("Enter a positive number of students.")
else:
    registrations = []
    for number in range(int(count_text)):
        print("\nStudent", number + 1)
        roll = input("Roll number: ").strip().upper()
        course_text = input("Course codes separated by spaces: ").upper().split()
        registrations.append((roll, tuple(course_text)))

    print("\nRegistration results:")
    seen_rolls = []
    invalid_rolls = []
    for roll, courses in registrations:
        errors = []
        if not roll:
            errors.append("roll number is required")
        elif roll in seen_rolls:
            errors.append("duplicate student record")
        else:
            seen_rolls.append(roll)
        if not courses:
            errors.append("at least one course is required")
        if len(courses) > 5:
            errors.append("more than 5 courses")

        reported = []
        for code in courses:
            if courses.count(code) > 1 and code not in reported:
                errors.append("duplicate course " + code)
                reported.append(code)
            if code not in known_courses:
                message = "unknown course " + code
                if message not in errors:
                    errors.append(message)
        if "CS201" in courses and "CS101" not in courses:
            errors.append("CS201 requires CS101")
        if "CS301" in courses and "CS201" not in courses:
            errors.append("CS301 requires CS201")
        if "CS301" in courses and "CS101" not in courses:
            errors.append("CS301 requires CS101")
        if "PHY101" in courses and "PHY102" in courses:
            errors.append("PHY101 and PHY102 cannot be combined")

        if errors:
            print((roll or "(blank)"), "INVALID:", "; ".join(errors))
            invalid_rolls.append(roll or "(blank)")
        else:
            print(roll, "VALID")
    print(f"Valid: {len(registrations) - len(invalid_rolls)} | Invalid: {len(invalid_rolls)}")
    if invalid_rolls:
        print("Students with violations:", ", ".join(invalid_rolls))
