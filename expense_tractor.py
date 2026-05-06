expenses = [
    {"name": "Food", "amount" : 1000},
    {"name": "Travel", "amount" : 500}
]

while True:
    print("1. Add expense")
    print("2. View expense")
    print("3. Total expense")
    print("4. exit")

    choice = input("Enter Choice :")

    if choice == "1" :
        name = input("Enter your name: ")
        amount = float(input("Enter your amount: "))

        expense = {"name": name, "amount": amount}
        expenses.append(expense)

    elif choice == "2":
        for e in expenses:
            print(e["name"], "-", e["amount"])

    elif choice == "3":
        total = 0

        for e in expenses:
            total += e["amount"]
            print("Total expense: ", total)

    elif choice == "4":
        break
