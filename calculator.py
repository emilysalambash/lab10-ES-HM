#calculator problem - Week 3 Lecture Problems
operation = str(input("Enter the operation: "))
number1 = float(input("Enter the first operand: "))
number2 = float(input("Enter the second operand: "))
if operation == "add":
    print(f"Result is {round(number1+number2,2)}")
elif operation == "sub":
    print(f"Result is {round(number1-number2,2)}")
elif operation == "mul":
    print(f"Result is {round(number1*number2,2)}")
elif operation == "div":
    print(f"Result is {round(number1/number2,2)}")

