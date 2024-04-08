UserInput = input("Escreva a expressão: ")

pair = {
    '(' : ')',
    '[' : ']',
    '{' : '}'
}

stack = []

for c in UserInput:
    if c in pair.keys():
        stack.append(c)
    elif c in pair.values():
        if len(stack) == 0:
            print(f"Erro na expressão em {c}")
            break
        else:
            t = stack.pop()
            if pair[t] != c:
                print(f"Erro na expressão em {c}")
                break

if len(stack) != 0:
    print(f"Erro na expressão! Incompleta")