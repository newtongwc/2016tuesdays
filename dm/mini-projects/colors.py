# A simple program to illustrate lists in Python

colors = ["red", "orange", "gold", "blue", "green", "purple", "crimson", "yellow"]
i = 0
while i < len(colors):
    print "When I was %d, my favorite color was %s." % (i, colors[i])
    i = i + 1
