cart = []

while True: 
    q = input("\n Buna ziua ce vreti sa faceti?? \n v- view shopping \n a- add obiect \n r- remove obiect\n q-quit \n ")

    if q.lower() == "v":
        if len(cart) == 0:
            print("Cosul tau este gol \n")
        for obiecte in cart:
            print(f"--{obiecte}--",end="")
    elif q.lower() == "a":
        q2 = input("Ce vreti sa adaugati in cos? \n")
        if q2 in cart:
            print("Este deja acest produs in cos")
        else:
            cart.append(q2)
    elif q.lower() == "r":
        q3 = input("Ce vrei sa scoti din cosul de cumparaturi? \n")
        cart.remove(q3)
    elif q.lower() == "q":
        print("Ai iesit din shopping cart")
        break
    else:
        print("INVALID")
        break


