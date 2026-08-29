print("===== Calculator with History =====")

history = []

while True:
    print("\n1. Calculate")
    print("2. Show History")
    print("3. Clear History")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        try:
            num1 = float(input("Enter first number: "))
            operator = input("Enter operator (+, -, *, /): ")
            num2 = float(input("Enter second number: "))

            if operator == "+":
                result = num1 + num2

            elif operator == "-":
                result = num1 - num2

            elif operator == "*":
                result = num1 * num2

            elif operator == "/":
                if num2 == 0:
                    print("Cannot divide by zero!")
                    continue
                result = num1 / num2

            else:
                print("Invalid operator!")
                continue

            calculation = f"{num1} {operator} {num2} = {result}"
            history.append(calculation)

            print("Result:", result)

        except ValueError:
            print("Please enter valid numbers!")

    elif choice == "2":
        print("\n===== Calculation History =====")

        if len(history) == 0:
            print("No history available.")
        else:
            for i, calculation in enumerate(history, start=1):
                print(f"{i}. {calculation}")

    elif choice == "3":
        history.clear()
        print("History cleared successfully!")

    elif choice == "4":
        print("Thank you for using the calculator!")
        break

    else:
        print("Invalid choice!")