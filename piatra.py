import random

optiuni = ("piatra",
           "hartie",
           "foarfece")
ai_score = 0
score = 0
is_playing = True

while is_playing:
    ai = random.choice(optiuni)
    question = input("Piatra Hartie sau Foarfece? \n")
    if question == "q":
        print("Sper ca ne am distrat!")
        break
    elif question not in optiuni:
        print("Nu stiu ce vrei")
        is_playing = False
    elif ai == question:
        print("\nEgalitate\n")
        print(f"Am avut amandoi {question}\n")
        print(f"Scorul este -{ai_score}- pentru mine si -{score}- pentru tine")
    elif ai == "foarfece" and question == "hartie":
        print("\nAi pierdut sefule \n")
        print(f"Eu am avut {ai}, iar tu ai avut {question}\n")
        ai_score += 1
        print(f"Scorul este -{ai_score}- pentru mine si -{score}- pentru tine")
    elif ai == "piatra" and question == "foarfece":
        print("\nAi pierdut sefule \n")
        print(f"Eu am avut {ai}, iar tu ai avut {question}\n")
        ai_score += 1
        print(f"Scorul este -{ai_score}- pentru mine si -{score}- pentru tine")
    elif ai == "hartie" and question == "piatra":
        print("\nAi pierdut sefule \n")
        print(f"Eu am avut {ai}, iar tu ai avut {question}\n")
        ai_score += 1
        print(f"Scorul este -{ai_score}- pentru mine si -{score}- pentru tine")
    else:
        print("\nBravo ai castigat! \n")
        print(f"Eu am avut {ai}, iar tu ai avut {question}\n")
        score += 1
        print(f"Scorul este -{ai_score}- pentru mine si -{score}- pentru tine")


