Texto = input("")

Vogais = 0

for letra in Texto:
    if letra in "aáàâãeéèêiíìîoóòôõuúùûAÁÀÂÃEÉÈÊIÍÌOÓÒÔÕUÚÙÛ":
        Vogais += 1

print(" ")
print("Existem: ", Vogais, "vogais")