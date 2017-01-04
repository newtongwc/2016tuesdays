#A simple program that uses arrays. It was written by Sara Manning.

colors = ["Red", "Blue", "Purple", "Yellow", "Green", "Orange"]

print("There are many colors in the world. Here are some examples.")

for i in range (1, (len(colors))+1):
    print("Example", i, " is" + colors[i-1])
    i = int(i)
