def get_number(prompt):
  """Gets a numerical input from the user with error handling."""
  while True:
    try:
      number = float(input(prompt))
      return number
    except ValueError:
      print("Invalid input. Please enter a number.")

def get_operation():
  """Gets the operation choice (+, -, *, /) from the user with error handling."""
  while True:
    operation = input("Choose operation (+, -, *, /): ")
    if operation in ["+", "-", "*", "/"]:
      return operation
    else:
      print("Invalid operation. Please enter +, -, *, or /.")

def calculate(num1, num2, operation):
  """Performs the calculation based on the chosen operation."""
  if operation == "+":
    return num1 + num2
  elif operation == "-":
    return num1 - num2
  elif operation == "*":
    return num1 * num2
  elif operation == "/":
    if num2 == 0:
      print("Error: Division by zero is not allowed.")
      return None  
    else:
      return num1 / num2

def main():
  """Main function to handle user interaction and calculation."""
  print("Welcome to the Simple Calculator!")
  num1 = get_number("Enter the first number: ")
  num2 = get_number("Enter the second number: ")
  operation = get_operation()

  result = calculate(num1, num2, operation)

  if result is not None: 
    print(f"{num1} {operation} {num2} = {result}")
  else:
    print("Calculation cannot be performed.")

if __name__ == "__main__":
  main()
