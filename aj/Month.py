print ("Hello!")
a = True
while (a == True) :
    b = input("What number month would you like to know the name of?")
    if (b==1):
        print ("Styczen")
    elif (b==2):
        print ("Luty")
    elif (b==3):
        print ("Marzec")
    elif (b==4):
        print ("Kwiecien")
    elif (b==5):
        print ("Maj")
    elif (b==6):
        print ("Czerwiec")
    elif (b==7):
        print ("Lipiec")
    elif (b==8):
        print ("Sierpien")
    elif (b==9):
        print ("Wrzesien")
    elif (b==10):
        print ("Pazdziernik")
    elif (b==11):
        print ("Listopad")
    elif (b==12):
        print ("Grudzien")
    else:
        print ("Month Unavailable")
    c = raw_input("Would you like another month")
    if (c== "no"):
        a = False
