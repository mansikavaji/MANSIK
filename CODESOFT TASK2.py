def calculator():
    # Prompt the user to enter the first number
    num1 = float(input("Enter the first number: "))
    
    # Prompt the user to enter the second number
    num2 = float(input("Enter the second number: "))
    
    # Display the operation choices
    print("Choose an operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    
    # Prompt the user to choose an operation
    choice = input("Enter your choice (1/2/3/4): ")
    
    # Perform the calculation based on the user's choice
    if choice == '1':
        result = num1 + num2
        operation = "+"
    elif choice == '2':
        result = num1 - num2
        operation = "-"
    elif choice == '3':
        result = num1 * num2
        operation = "*"
    elif choice == '4':
        if num2 != 0:
            result = num1 / num2
            operation = "/"
        else:
            result = "undefined (division by zero is not allowed)"
            operation = "/"
    else:
        result = "Invalid choice"
        operation = ""
    
    # Display the result
    if operation:
        print(f"{num1} {operation} {num2} = {result}")
    else:
        print(result)

# Run the calculator
calculator()
