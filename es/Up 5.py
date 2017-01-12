import time
print"I'm going to count up by 5 to 100"
current5 = 5
while True:
    print (current5)
    time.sleep(.5)
    current5 = current5 + 5
    if current5 == 105:
       print"Done!"
       current5 = current5 - 100
