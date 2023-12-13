def base10to2():
    pass

def base2to10(binaryNumber):
    add = 0
    expoent = len(binaryNumber) - 1
    for position in range(len(binaryNumber)):
        if binaryNumber[position] == "1":
            add = add + 2 ** expoent
        expoent = expoent - 1
    return add

def main():
    while True:
        print("1 - Convert base10 to base2")
        print("2 - Convert base2 to base10")
        print("0 - Close program")

        Selection = int(input(""))

        if Selection == 1:
            N = int(input("Type the number: "))
            base10to2(N)

        if Selection == 2:
            N = int(input("Type the number: "))
            print("")
            print(base2to10(N))
            print("")

        if Selection == 0:
            exit()

if __name__ == "__main__":
    main()