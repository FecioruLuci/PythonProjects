quests = ("Care este cel mai rapid animal? \n",
          "Care este cel mai bogat om? \n",
          "Care este cel mai popular limbaj de programare? \n",
          "Care este cel mai popular brand de masini? \n")

options = (("A-maimuta","B-crocodil","C-leopard","D-caine"),
           ("A-Cristiano Ronaldo","B-Presedintele Romaniei","C-Elon Musk","D-Bill Gates"),
           ("A-Python","B-C++","C-JavaScript","D-Assembly"),
           ("A-Ferrari","B-Audi","C-BMW","D-Porche"))

answers = ("C",
           "C",
           "A",
           "C")

guesses = []

score = 0

quest_count = 0

for quest in quests:
    print("--------------")
    print(quest, end="")
    print("--------------")
    for option in options[quest_count]:
        print(option)
    

    guess = input("Scrie care este varianta corecta \n").upper()

    if guess == answers[quest_count]:
        score += 1
        print("Corect")
    else:
        print("Gresit")
    quest_count += 1
print(f"Scorul tau este de: {score}")