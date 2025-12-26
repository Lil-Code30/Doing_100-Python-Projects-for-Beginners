print("=== Calculator ===")

num1 = float(input("Enter the first number: "))

operator = input("Enter operation (+, -, *, /): ")

num2 = float(input("Enter the second number: "))

match operator:
    case "+":
        print(f"Result: {num1 + num2}")
    case "-":
        print(f"Result: {num1 - num2}")
    case "*":
        print(f"Result: {num1 * num2}")
    case "/":
        if(num2 == 0 ):
            print("the denominator should not be zero.")
        else:    
            print(f"Result: {num1 / num2}")
    case _:
        print("Error!! Wrong operator.")

