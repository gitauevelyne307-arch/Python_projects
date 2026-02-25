# Exercises

# 1: Python Calculator(Using If statements)

operator = input("Enter an operator(+, -, *, /): ")
num1 = float(input("Enter num1: "))
num2 = float(input("Enter num2: "))

if operator == "+":
    result = (num1 + num2)
    print(round(result,2))
elif operator == "-":
    result = (num1 - num2)
    print(round(result,2))
elif operator == "*":
    result = (num1 * num2)
    print(round(result,2))
elif operator == "/":
    result = (num1 / num2)
    print(round(result,2))
else:
    print(f"{operator} is not a valid operator")

# 2: Python Weight Converter

weight = float(input("Enter your weight: "))
unit = input("Kilograms or Pounds? (K or L): ")

if unit == "K":
    weight = weight * 2.205
    unit = "Lbs."
    print(f"Your weight is: {round(weight, 1)} {unit}")
elif unit == "L":
    weight = weight/2.205
    unit = "Kgs."
    print(f"Your weight is: {round(weight, 1)} {unit}")
else:
    print(f"{unit} is not a valid unit")

# 3: Temperature conversion programme

unit = input("Is the temperature in Celsius or Fahrenheit? (C/F): ")
temp = float(input("Enter the temperature: "))
if unit == "C":
    temp = round((temp * 9) / 5 + 32, 1)
    print(f"The temperature in Fahrenheit is: {temp}F")
elif unit == "F":
    temp = round((temp * 9) / 5 - 32, 1)
    print(f"The temperature in Celsius is: {temp}C")
else:
    print(f"{unit} is not a valid unit of measurement")


# 4: Grading system

grade = int(input("Enter your grade: "))

if grade < 0 or grade > 100:
    print("Invalid score")
elif grade >= 80:
    print("Grade A: Excellent")
elif grade >= 60:
    print("Grade B: Good Job")
elif grade >= 40:
    print("Grade C: Fair")
else:
    print("Fail: Needs improvement")

# 5: ATM Withdrawal program

balance = float(input("Enter your balance: "))
withdrawal_amount = float(input("Enter amount to withdraw: "))

if withdrawal_amount <= 0:
    print("Invalid withdrawal amount")
elif withdrawal_amount > balance:
    print("Withdrawal amount cannot be greater than balance")
elif withdrawal_amount > 10000:
    print("Withdrawal amount cannot be greater than 10,000")
else:
    balance = balance - withdrawal_amount
    print("Withdrawal successful")
    print("Remaining balance is: ", balance)

