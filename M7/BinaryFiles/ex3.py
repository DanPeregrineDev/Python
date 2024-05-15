import pickle

values = []

nV = int(input("Quantos valores quer inserir: "))

for i in range(nV):
    value = int(input(f"Valor {i + 1}: "))
    values.append(value)
    

with open('ex3.pkl', 'ab') as file:
    pickle.dump(values, file)