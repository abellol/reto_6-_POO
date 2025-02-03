# Reto 6 POO
Hola, soy **Alejandro Bello** y pertenezco al grupo fenomenoides, a continuación nuestro logo:

<details><summary>Preparense para ver el grandioso logo: </summary><p>
<div align='center'>
<figure> <img src="https://i.postimg.cc/NFbwf57S/logo-def.png" alt="Logo fenomenoides" width="400" height="auto"/></br>
<figcaption><b> "somos programadores, no diseñadores" </b></figcaption></figure>
</div>
</p></details><br>

#### Excepciones para el reto 1
##### 1. Crear una función que realice operaciones básicas (suma, resta, multiplicación, división) entre dos números, según la elección del usuario, la forma de entrada de la función será los dos operandos y el caracter usado para la operación.
```python
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
```

###### 2. Realice una función que permita validar si una palabra es un palíndromo. Condición: No se vale hacer slicing para invertir la palabra y verificar que sea igual a la original

```python
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
```
##### 3. Escribir una función que reciba una lista de números y devuelva solo aquellos que son primos. La función debe recibir una lista de enteros y retornar solo aquellos que sean primos.
```python
def is_prime(number:int)->bool:
  """
  Function to verify if a number is prime or not.

  Args: 
    number: The number to verify (int)

  Returns: 
    a bool value if the number is prime or not.
  """
  prime : bool = True 

  # Searching divisors from 2 to the half of the number
  index : int = (number // 2) + 1 
  for i in range(2, index):
    if number % i == 0: # If a divisor is founded, the number isn't prime
      prime = False 
      break
  return prime

def find_primes(numbers:list)->list:
  """
  Function to find primes into a list

  Args: 
    numbers: A list with numbers (list)

  Returns:
    The function returns a list with the prime numbers into the list.
  """

  prime_list : list = [] # Empty list to save prime numbers founded

  # Accesing for every number in the list
  for number in numbers:
    if number == 1: continue # "1" is a special case, it's discarded

    if is_prime(number) == True: # Calling the function to verify each number in the list
      prime_list.append(number) # The prime ones were saved in the empty list
    else:
      continue
  return prime_list

if __name__ == "__main__":
  try:
    test_list = [1, 2, 3, 4, 5, 6, 7, 53, 57, 59, 60, 62] # Example list
    primes = find_primes(test_list) # Calling the function
    print(primes)
  except TypeError:
    print("Invalid types")
```
##### 4. Escribir una función que reciba una lista de números enteros y retorne la mayor suma entre dos elementos consecutivos.
```python
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
```
##### 5. Escribir una función que reciba una lista de string y retorne unicamente aquellos elementos que tengan los mismos caracteres.
```python
def same_letters(list_words: list) -> list:
  """
  Function to find the words with the same letters in a list.

  Args:
    list_words: A list with words (list)

  Returns:
    The function returns a list with the words that have the same letters.
  """
  words = {} # empty dictionary to save the words with the same lexicographic order
  result = [] # empty list to save the words with the same letters

  for word in list_words:
    valor = "".join(sorted(word)) # Ordering the word by lexicographic order and using it as key, and saving the original word
    if valor in words.keys():
      words[valor] += [word]
    else:
      words[valor] = [word]
  
  for value in words.values(): # if the key (the lexicographic order of a word) has two or more words, they have the same letters
    if len(value) >= 2:
      result += value

  return result 

if __name__ == "__main__":
  try:
    test_list : list = ["roma", "amor", "perro", "ropa", "pora", "mora", "juan", "porre"]
    print(same_letters(test_list))
  except TypeError: 
    print("Invalid types")
```
