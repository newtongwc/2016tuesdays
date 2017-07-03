while True:
    currentNumber = 0
    userNumber = input("Give me a number -->")
    for number in range(1, userNumber + 1):
        print "%i + %i = %i" % (currentNumber, number, number + currentNumber)
        currentNumber = currentNumber + number
    print "The value of all the digits in your number is %i" % currentNumber
