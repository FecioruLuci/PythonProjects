import random

def rotire():
    fructe = ["🍇","🍒","🍎"]
    lista = []

    for fruct in range(3):
        lista.append(random.choice(fructe))
    return lista

def plata(pariu):
    platire = pariu * 100
    return platire

def main():
    balanta = 100
    print("-------------------------\n")
    print("Bine ai venit la pacanele\n")
    print("-------------------------\n")
    while balanta > 0:
        print(f"Balanta ta este de {balanta}ron")
        pariu = input("Cat doriti sa pariati? \n")
        if not pariu.isdigit():
            print("INVALID")
            continue
        else:
            pariu = int(pariu)
        if pariu > balanta:
            print("Nu poti paria mai mult decat balanta ta\n")
            continue
        if pariu <= 0:
            print("Nu poti paria o valoare negativa\n ")
            continue

        balanta -= pariu
        linia = rotire()
        print(" ".join(linia))
        cashout = plata(pariu)
        if linia[0] == linia[1] == linia[2]:
            print("Felicitari ai prins jackpot-ul \n")
            balanta += cashout

if __name__ == "__main__":
    main()