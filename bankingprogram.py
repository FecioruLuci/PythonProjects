def showbalance(balanta):
    print(f"Balanta dumneavoastra este de: {balanta:.2f}lei \n")

def  deposit(balanta,bani):
    balanta += bani
    print("Depozitarea s-a facut cu succes \n")
    return balanta

def withdraw(balanta,scoate):
    balanta -= scoate
    print(f"Ati scos suma de {scoate}lei")
    return balanta

def exit():
    print("Ati iesit din program")
    return False


on = True
balanta = 0
question_nume = input("Cum va numiti domnule? \n")
if not question_nume.isdigit():
    print(f"Bine ati venit {question_nume}")
while on:
    print("----------------")
    print("1-ShowBalance \n 2-Deposit \n 3-Withdraw \n 4-Exit \n")
    question = input("Buna ziua ce doriti sa faceti? \n")

    if question == "1":
        showbalance(balanta)
    if question == "2":
        bani = float(input("Cat doriti sa depozitati? \n"))
        if bani > 0:
            balanta = deposit(balanta,bani)
        else:
            print("Ne pare rau dar nu puteti sa depozitati o suma negativa! \n")
    if question == "3":
        scoate = float(input("Cat doriti sa scoateti? \n"))
        if scoate < balanta:
            balanta = withdraw(balanta,scoate)
        else:
            print(f"{question_nume}, ne pare rau dar nu puteti sa scoateti aceasta suma \n")
    if question == "4":
        on = exit()