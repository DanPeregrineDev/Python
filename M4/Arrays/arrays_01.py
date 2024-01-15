import numpy as np 

# Create an empty array with 5 positions
array = np.empty(5)

# Prints the array
print(array)

print("") # Blank line
# Prints the value in the 2nd position
print(array[2])

print("")
# Subtracts -7 to the value in the 3rd position
array[3] = array[3] - 7
print(array)

print("")
# Data inputs
for i in range(5): # 5 positions
    array[i] = int(input(f"Insira o {i + 1}º numero: "))

print(array)

print("")
# Runs through the array by the values
for x in array:
    print(x)

print("")
#  Runs through the array by the positions
for i in range(5):
    print(array[i])