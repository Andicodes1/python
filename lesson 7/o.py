def perform_operation(number1, number2, operator):
    if operator == "+":
        return number1 + number2
    elif operator == "-":
        return number1 - number2
    elif operator == "*":
        return number1 * number2
    elif operator == "/":
        if number2 == 0:
            raise ZeroDivisionError("Error: Division by zero is not allowed.")
        return number1 / number2
    else:
        raise ValueError("Error: Invalid operator. Please use +, -, *, or /.")


try:

    number1 = float(input("Enter the first number: "))
    number2 = float(input("Enter the second number: "))
    operator = input("Enter the operator (+, -, *, /): ")


    result = perform_operation(number1, number2, operator)


    print(f"The result of {number1} {operator} {number2} is: {result}")

except ValueError as ve:
    print(ve)
except ZeroDivisionError as zde:
    print(zde)
except Exception as e:
    print(f"An unexpected error occurred: {e}")
finally:
    print("End of program.")
