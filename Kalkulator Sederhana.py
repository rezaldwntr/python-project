# Step 1: Get user input for two numbers
number1 = float(input("Enter the first number: "))
number2 = float(input("Enter the second number: "))

# Step 2: Perform arithmetic operation
addition = number1 + number2
subtraction = number1 - number2
multiplication = number1 * number2
division = number1 / number2 if number2 != 0 else "Cannot divide by zero"
floor_division = number1 // number2 if number2 != 0 else "Tidak bisa dibagi 0"
modulus = number1 % number2 if number2 != 0 else "Tidak bisa dibagi 0"
exponentiation = number1 ** number2

# Step 3: Display the results
print("\n--- Calculator Results ----")
print(f"Addition:{number1} + {number2} = {addition}")
print(f"Subtraction:{number1} - {number2} =  {subtraction}")
print(f"Multiplication:{number1} x {number2} =  {multiplication}")
print(f"Division:{number1} / {number2} =  {division}")
print(f"Floor Division:{number1} / {number2} = {floor_division}")
print(f"Modulus:{number1} % {number2} = {modulus}")
print(f"Exponentiation:{number1} ** {number2} = {exponentiation}")
