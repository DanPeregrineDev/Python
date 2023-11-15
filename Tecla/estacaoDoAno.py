CurrentDay = int(input("Em que dia do ano está?: "))

if CurrentDay > 355 or CurrentDay < 78:
    print("Inverno")

if CurrentDay > 78 and CurrentDay < 171:
    print("Primavera")

if CurrentDay > 171 and CurrentDay < 264:
    print("Verão")

if CurrentDay > 264 and CurrentDay < 355:
    print("Outono")