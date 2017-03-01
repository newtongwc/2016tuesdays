def summativeProgram():
    number = input("Type a number to find its summative. ")
    i = 0
    finalNumber = 0
    for i in range (0, number):
        finalNumber = finalNumber + number
        number = number - 1
        print(finalNumber)
        print("Adding:")
        print(number)
    print("Here is the final result:")
    print(finalNumber)
summativeProgram()
