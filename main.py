import lotteri
import os


lotteriet = lotteri.Lotteri()

looping=True

while looping:

    os.system("cls" if os.name == "nt" else "clear")
    antal_lotter=input("\n\t\t ")


    try:
        int_antal_lotter = int(antal_lotter)
        i = 0 

        if (int_antal_lotter < 4): 
             os.system("cls" if os.name == "nt" else "clear")
             print("\n\t\tGrattis du vann det här!!!!")

             while i < int_antal_lotter :
                 vinst = lotteriet.get_vinst()
                 print("\t\t" + vinst)
                 i+=1

        elif(int_antal_lotter > 3):
            print("\n\t\t du har valt för många lotter")

        


    except ValueError:
        print("\n\t\terror")


    print("--------------------------------------")
    spela_igen = input("\n\t\t Vill du spela igem? j/ n/ ")
    if (spela_igen=="n"):
        break