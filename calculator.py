print("MY CALCULATOR")
num1 = float(input("Enter Your First Number:"))
num2 = float(input("Enter Your Second Number:"))
operation = input("Pick An Operation: (+, -, *, /): ")
if operation == "+":
    print("The Answer Is =", num1 + num2)
elif operation == "-":
    print("The Answer Is =", num1 - num2)
elif operation == "*":
    print("The Answer Is =", num1 * num2)
elif operation == "/":
    if num2 != 0:
        print("The Answer Is=", num1 / num2)
    else:
        print("Cannot Divided By Zero")
else:
    print("Invalid Operation! Please Try Again...")
    
