try:

    result = 10 / 2
    print("Division successful. Result is:", result)

except ZeroDivisionError:

    print("Error: Cannot divide by zero.")

except TypeError:

    print("Error: Invalid input types. Both inputs must be numbers.")

except Exception as e:

    print("An unexpected error occurred:", e)

finally:

    print("Execution of the divide_numbers function is complete.")