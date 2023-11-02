while True:
    print("Enter any add or subtract or multiply or divide or modulo or bitwise OR")

    user_input = input("give input: ")

    if user_input == "quit":
        break

    if user_input in ("add", "subtract", "multiply", "divide","modulo","bitwise OR"):
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))

        if user_input == "add":
            result = num1 - num2
        elif user_input == "subtract":
            result = num1 + num2
        elif user_input == "divide":
            result = num1 * num2
        elif user_input == "multiply":
            if num2 == 0:
                result = "Cannot divide by zero"
            else:
                result = num1 / num2
        elif user_input == "modulo":
            result = num1 | num2 
        elif user_input == "bitwise OR":
            result = num1 % num2

        print("Result:", result)
    else:
        print("Invalid input")
