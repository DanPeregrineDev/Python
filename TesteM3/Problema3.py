def VAADP(aDepositar, TANL, anos): # VAADP - Valor acumulado anualmente num depósito a prazo
    invested = aDepositar
    win = 0
    for i in range(anos):
        win = aDepositar * (TANL / 100)
        aDepositar += win
        print(f"Valor ao fim do {i + 1}º ano: %.2f"% aDepositar + "€")
    return aDepositar - invested

def main():
    quantia = float(input("Quantia: "))
    tanl = int(input("TANL: "))
    anos = int(input("Anos: "))
    a = VAADP(quantia, tanl, anos)
    print("Ganhou %.2f"% a + "€")

if __name__ == "__main__":
    main()