import random


low = 1
high = 100
valoarea = random.randint(low,high)
is_playing = True

while is_playing:
    question = int(input("La ce numar crezi ca m-am gandit?(intre 1 si 100) \n"))

    if question > valoarea:
        print("Este putin cam mare numarul tau\n")
    elif question < valoarea:
        print("Este putin cam mic numarul tau\n")
    else:
        print("Ai ghicit numarul :)\n")
        question2 = input("Mai vrei sa joci?\n")
        if question2.lower() == "da":
            valoarea = random.randint(low,high)
            continue
        else:
            break

