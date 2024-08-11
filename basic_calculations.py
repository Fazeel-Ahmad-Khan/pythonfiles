#1. Input and Operations
#- Option 1: User Input
def calculator():
  num1 = float(input("Enter first number: "))
  num2 = float(input("Enter second number: "))
  operator = input("Enter operation (+, -, *, /): ")

  if operator == '+':
    result = num1 + num2
  elif operator == '-':
    result = num1 - num2
  elif operator == '*':
    result = num1 * num2
  elif operator == '/':
    if num2 == 0:
      print("Error: Division by zero")
    else:
      result = num1 / num2
  else:
    print("Invalid operator")
  print("Enter first number:", num1)
  print("Enter first number:", num2)
  print("Enter operation (+, -, *, /):", operator)
  print("Result:", result)

calculator()

# Option 2: Variables
a = 10
b = 5

sum = a + b
print("Sum:", sum)

difference = a - b
print("Difference:", difference)

product = a * b
print("Product:", product)

if b != 0:
  quotient = a / b
  print("Quotient:", quotient)
else:
  print("Error: Division by zero")
