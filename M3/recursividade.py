def exponenciacao(base, expoente):
    if expoente == 1:
        return base
    else:
        return exponenciacao(base, expoente - 1) * base
    
print(exponenciacao(4, 3))