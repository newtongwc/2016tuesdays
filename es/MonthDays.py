while True:
    print "Type in a month's and learn how many days it has."
    month = raw_input()
    if month.lower() == "january":
        print "31"
    elif month.lower() == "february":
        print "28"
    elif month.lower() == "march":
        print "31"
    elif month.lower() == "april":
        print "30"
    elif month.lower() == "may":
        print "31"
    elif month.lower() == "june":
        print "30"
    elif month.lower() == "july":
        print "31"
    elif month.lower() == "august":
        print "31"
    elif month.lower() == "september":
        print "29"
    elif month.lower() == "october":
        print "31"
    elif month.lower() == "november":
        print "30"
    elif month.lower() == "december":
        print "31!"
    else:
        print "Type a month"
