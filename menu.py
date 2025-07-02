menu = {"cola": 9.99,
        "fanta": 9.99,
        "ceai": 12.99,
        "coctail": 17.99,
        "vodka": 19.99}

for key, value in menu.items():
    print("----------------")
    print(f"{key:10} : {value:.2f} lei")
    print("----------------")

cart = []
total = 0

comanda = True
while comanda:
    question = input("Ce doriti sa comandati? q ca sa iesiti| v-sa vedeti cosul de cumparaturi\n")
    if question.lower() == "q":
        print("Ati iesit din program\n" )
        comanda = False
    elif question.lower() == "v":
        if cart:
            print("Produsele din cos \n")
            for item in cart:
                print(f"{item}")
        else:
            print("Nu ai nimica in cos! \n")
    elif menu.get(question) is not None:
        cart.append(question)
    else:
        print("Nu dispunem de acest produs \n")
print(cart)
for element in cart:
    total += menu.get(element)
print(f"Totalul este de {total} lei")