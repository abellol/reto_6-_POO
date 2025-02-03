def higher_sum(numbers : list)-> int: 
  """
  Function to calculate the higher sum between two consecutive numbers in the list.

  Args:
    numbers: List of numbers (list)

  Returns:
    The function returns the higher sum between two numbers
  """

  high = 0 # Starting value for the sume

  # Accesing to every pair of consecutive elements on the list
  for i in range(len(numbers)-1): # Accesing to the index and the next one to the right
    aux = numbers[i] + numbers[i+1] 
    if aux > high: # If the sum is higher than the last value, it replaces it
      high = aux
  return high

if __name__ == "__main__":
  try:
    test_list = [2, 24, 17, 6, 7, "43"] # Example list
    high_sum = higher_sum(test_list) # Call to the function
    print(high_sum)
  except TypeError:
    print("Invalid types")