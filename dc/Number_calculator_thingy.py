n = input ("Type a number (only one (but it can be multiple digits))\n--->")

math = 1

for number in range(2, n+1):
    print "%d+%d=%d" % (math, number, number + math)
    math += number
print "The answer is %d" % math





















