def palindrome(word:str) -> bool:
  """
  Function to verify if a word is a palindrome, without slicing.

  Args: 
    word: The word to verify (string)

  Returns: 
    a boolean value to show f the word is or not a palindrome
  """

  reversed : str = "" # Variable to save each letter from the reversed word

  # Reversing the word
  for i in range(-1, -(len(word)+1), -1):  
    reversed += (word[i])

  if word == reversed:
    return True
  else:
    return False
  
if __name__ == "__main__":
  try:
    word : str = input("Enter a word to verify if a word is a palindrome: ") # input from de user
    is_palindrome = palindrome(word) # Calling the function
    print(is_palindrome)
  except ValueError:
    print("Invalid input")
  
