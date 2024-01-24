# Taxas locais: EEE - 0,234/min Resto da Europa - 0,735/min America e Africa 0,762/min Asia e Oceania 1,872/min
# Chamadas video - 1,272/min

TipoDeChamada = input("Tipo de chamada (Voz ou Vídeo): ").upper()
Local = input("Região (EEE, Resto Europa, América e África, Asia e Oceânia): ").upper()
Duracao = int(input("Duração da chamada (Em segundos): "))

# Voz

if TipoDeChamada == "VOZ":
    # EEE
    if Local == "EEE":
        taxa = 0.234
    elif Local == "RESTO EUROPA":
        taxa = 0.735
    elif Local == "AMÉRICA E ÁFRICA" or Local == "AMERICA E ÁFRICA" or Local == "AMÉRICA E AFRICA" or Local == "AMERICA E AFRICA":
        taxa = 0.762
    elif Local == "ASIA E OCEÂNIA" or Local == "ASIA E OCEANIA":
        taxa = 1.872
    else:
        print("ERRO: TIPO DE CHAMADA(VOZ)")

# Video

if TipoDeChamada == "VÍDEO" or TipoDeChamada == "VIDEO":
    taxa = 1.272

# Converter para minutos

Minutos = int(Duracao / 60)

# Total

Total = taxa * Minutos

print(f"O valor a pagar é %.2f"% Total + "€")