import numpy as np

names = np.empty(5, dtype="U20") # U - Unicode | 20 - max 20 characters

names[0] = "Joaquim"
names[1] = "Maria"
names[2] = "António"

print(names[0])
print(names[1])