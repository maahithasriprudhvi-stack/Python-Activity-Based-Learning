# Case study 2: Progressive Electricity Billing
# Charges are calculated separately for every slab.

count_text = input("Number of months: ").strip()
if not count_text.isdecimal() or int(count_text) < 1:
    print("Enter a positive number of months.")
else:
    previous_units = None
    previous_bill = None
    for number in range(int(count_text)):
        print("\nMonth", number + 1)
        month = input("Month name: ").strip()
        units_text = input("Units consumed: ").strip()
        if not month or not units_text.isdecimal():
            print("Invalid month or units; record skipped.")
            continue

        units = int(units_text)
        if units <= 100:
            energy = units * 3
        elif units <= 200:
            energy = 100 * 3 + (units - 100) * 5
        else:
            energy = 100 * 3 + 100 * 5 + (units - 200) * 7

        fixed = 50
        surcharge = 0
        if units > 300:
            surcharge = energy * 0.05
        rebate = 0
        if previous_units is not None and units < previous_units:
            rebate = energy * 0.05
        bill = energy + fixed + surcharge - rebate

        print(f"{month}: energy Rs {energy:.2f}, fixed Rs {fixed:.2f}, "
              f"surcharge Rs {surcharge:.2f}, rebate Rs {rebate:.2f}")
        print(f"Bill: Rs {bill:.2f}")
        if previous_bill is not None:
            change = (bill - previous_bill) * 100 / previous_bill
            print(f"Bill change: {change:+.2f}%")
            if change > 30:
                print("Unusual increase: more than 30%")
        previous_units = units
        previous_bill = bill
