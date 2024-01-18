def convertTime(seconds):
    if seconds < 0:
        print("O valor dos segundos não pode ser negativo")
        return

    minutes = int(seconds / 60)
    fSeconds = seconds - (60 * minutes)
    print(f"O Tempo total foi {minutes}:{fSeconds}")

def main():
    convertTime(int(input("Tempo obtido na prova (em segundos): ")))


if __name__ == "__main__":
    main()