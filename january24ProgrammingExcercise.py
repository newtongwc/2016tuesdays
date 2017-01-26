def daysOfMonth():
    thirtyDays = ["September", "November", "April", "June"]
    thirtyOneDays = ["January", "March", "May", "July", "August", "October","December"]
    #February does not need to be a variable

    userInput = raw_input("Type in a month to find out how many days it has.")

    if userInput == "February":
        print("This month as 28 days.")
    else:
        for month in range (len(thirtyDays)):
            if userInput == thirtyDays[month]:
                print("This month has thirty days.")
        for month in range (len(thirtyOneDays)):
            if userInput == thirtyOneDays[month]:
                print("This month has thirty-one days.")

    # while True:
    #     userInput = ("Would you like to find the number of days for another month? Type yes or no exactly.")
    #     if userInput == "yes":
    #         daysOfMonth();
    #         break
    #     elif userInput == "no":
    #         print("Thank you for using this program.")
    #         break
    #     else:
    #         print("Please type yes or no exactly.")
daysOfMonth()
