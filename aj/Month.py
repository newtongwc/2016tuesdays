print ("Hello!")
a = True
while (a == True) :
    b = input("What number month would you like to know the name of?")
    if (b==1):
        print ("Styczen")
        print ("31 Days")
    elif (b==2):
        print ("Luty")
        c = input("What year is it?")
        if (c%4 == 0):
            print("29 Days")
        else:
            print ("28 Days")
    elif (b==3):
        print ("Marzec")
        print ("31 Days")
    elif (b==4):
        print ("Kwiecien")
        print ("30 Days")
    elif (b==5):
        print ("Maj")
        print ("31 Days")
    elif (b==6):
        print ("Czerwiec")
        print ("30 Days")
    elif (b==7):
        print ("Lipiec")
        print ("31 Days")
    elif (b==8):
        print ("Sierpien")
        print ("31 Days")
    elif (b==9):
        print ("Wrzesien")
        print ("30 Days")
    elif (b==10):
        print ("Pazdziernik")
        print ("31 Days")
    elif (b==11):
        print ("Listopad")
        print ("30 Days")
    elif (b==12):
        print ("Grudzien")
        print ("31 Days")
    else:
        print ("Month Unavailable")
    c = raw_input("Would you like another month")
    if (c== "no"):
        a = False
