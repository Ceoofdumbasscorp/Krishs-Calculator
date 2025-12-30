print("Welcome to The Krish Calculator!" +
      "\nThese are the allowed operations: ")
i = 0
j = 0
operations = ["+", "-", "*", "/"]
for op in operations:
    print(op)
validRun = True
while(validRun):
    number1 = int(input("Please enter the first number you want: "))
    op = input("What Operator would you like? ")
    number2 = int(input("Please enter the second number you want: "))

    if op == "+":
        sum = number1 + number2
    elif op == "-":
        sum = number1 - number2
    elif op == "*":
        sum = number1 * number2
    elif op == "/":
        sum = number1 / number2
        print("INVALID OPERATIONS TRY AGAIN")

    calc = "Calculating"
    for i in range(3):
        calc += "."
    print(calc)
    print(f"The answer to {number1} {op} {number2} is: {sum}")

    runAgain = input("Would you like to perform another calculation? (y/n): ")
    if runAgain.lower() != 'y':
        validRun = False
        print("Thank you for using The Krish Calculator! Goodbye!")
    