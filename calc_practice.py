num1 = float(input("Enter First Number: ")) #can also do 'int'
op = input("Operator: ")
num2 = float(input("Enter Second Number: "))

if op == "+":
    print(num1 + num2)
elif op == "-":
    print(num1 - num2)
elif op == "/":
    print(num1 / num2)
elif op == "*":
    print(num1 * num2)
else:
    print("Error - Invalid Operation. Try Again.")