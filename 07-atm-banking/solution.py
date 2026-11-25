# Case study 38: ATM Menu-Driven Banking Simulation
# All amounts are whole rupees and the balance is not saved after exit.

balance = 5000
transactions = []
print("Opening balance: Rs 5000")

while True:
    print("\n1 Deposit | 2 Withdraw | 3 Balance | 4 Statement | 0 Exit")
    choice = input("Choice: ").strip()

    if choice == "1" or choice == "2":
        amount_text = input("Amount: ").strip()
        if not amount_text.isdecimal() or int(amount_text) == 0:
            print("Enter a positive whole number of rupees.")
            continue
        amount = int(amount_text)
        if choice == "1":
            if amount > 100000:
                print("Deposit limit is Rs 100000.")
            else:
                balance += amount
                transactions.append(("Deposit", amount, balance))
                print(f"Deposited Rs {amount}. Balance: Rs {balance}")
        else:
            if amount % 100 != 0:
                print("Withdrawal must be a multiple of Rs 100.")
            elif amount > 10000:
                print("Withdrawal limit is Rs 10000.")
            elif balance - amount < 1000:
                print("Minimum balance of Rs 1000 must remain.")
            else:
                balance -= amount
                transactions.append(("Withdraw", amount, balance))
                print(f"Withdrawn Rs {amount}. Balance: Rs {balance}")
    elif choice == "3":
        print(f"Balance: Rs {balance}")
    elif choice == "4":
        print("Transaction statement:")
        if not transactions:
            print("No successful transactions.")
        for kind, amount, new_balance in transactions:
            print(f"{kind}: Rs {amount} | Balance: Rs {new_balance}")
        print(f"Current balance: Rs {balance}")
    elif choice == "0":
        print(f"Closing balance: Rs {balance}")
        break
    else:
        print("Invalid choice.")
