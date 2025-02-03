def basic_operations(number_1:float, number_2:float, operation:str) -> float:
  """
  Function to operate two numbers with the basic operations.

  Args: 
    Number_1: First num to operate (float)
    Number_2: Second num to operate (float)
    Operation: The symbol to march the operation (string)

  Returns:
    The function returns the result of the operation wanted
  """

  # Match case for each operation case (+, - , *, /)
  match operation:
    case "+":
      return number_1 + number_2
    case "-":
      return number_1 - number_2
    case "*":
      return number_1 * number_2
    case "/":
      return number_1 / number_2
    case _: # Default case if no one match
      return "Invalid operation"

if __name__ == "__main__":

  # Saving the data provided by the user
  try:
    number_1 = float(input("Enter your first number: ")) 
    number_2 = float(input("Enter your second number: "))
    operation : str = input("Enter your operation (+, -, *, /): ")
    #Calling the function
    operations = basic_operations(number_1, number_2, operation)
    print(operations)
  except ValueError:
    print("Invalid input")




