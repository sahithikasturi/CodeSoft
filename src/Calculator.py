def main():
    print("Simple Calculator")
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        
        print("\nSelect operation:")
        print("1. Addition (+)")
        print("2. Subtraction (-)")
        print("3. Multiplication (*)")
        print("4. Division (/)")
        operation = input("Enter choice (1/2/3/4): ")
        
        if operation == '1':
            result = num1 + num2
            print(f"\nResult: {num1} + {num2} = {result:.2f}")
        elif operation == '2':
            result = num1 - num2
            print(f"\nResult: {num1} - {num2} = {result:.2f}")
        elif operation == '3':
            result = num1 * num2
            print(f"\nResult: {num1} * {num2} = {result:.2f}")
        elif operation == '4':
            if num2 == 0:
                print("\nError: Division by zero is not allowed.")
            else:
                result = num1 / num2
                print(f"\nResult: {num1} / {num2} = {result:.2f}")
        else:
            print("\nInvalid operation choice. Please select 1, 2, 3, or 4.")
    except ValueError:
        print("\nInvalid input. Please enter numeric values.")

if __name__ == "__main__":
    main()