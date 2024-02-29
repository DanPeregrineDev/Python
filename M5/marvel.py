import random

superHeroes = ["Spider Man", "Iron Man", "Captain America", "Thor", "Hulk", "Black Panther", "Doctor Strange", "Vision"]
superVilains = ["Magneto", "Doctor Doom", "Thanos", "Loki", "Galactus", "Kingpin", "Green Goblin", "Vonon"]

while len(superHeroes) > 0:
    currentHero = superHeroes[random.randint(0, len(superHeroes) - 1)]
    currentVilain = superVilains[random.randint(0, len(superVilains) - 1)]

    print(f"{currentHero} VS {currentVilain}")

    winner = random.randint(1, 2)

    if winner == 1:
        winner = currentHero
    elif winner == 2:
        winner = currentVilain

    print(f"{winner} é o vencedor")

    superHeroes.remove(currentHero)
    superVilains.remove(currentVilain)

    print("")