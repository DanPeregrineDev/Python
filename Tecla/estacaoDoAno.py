CurrentDay = int(input("Em que dia do ano está?: "))

if CurrentDay > 355 or CurrentDay < 78:
    print("Inverno")

if CurrentDay > 78 or CurrentDay < 171:
    print("Primavera")

if CurrentDay > 171 or CurrentDay < 264:
    print("Verão")

if CurrentDay > 264 or CurrentDay < 355:
    print("Outono")