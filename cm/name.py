name = raw_input("Please enter your name ---> ")

# Put name in all caps.
name = name.upper()

print "Look, I made your name into an N!"

# Loop over all the letters in the name. A range based for loop keeps
# track of whether we're on the first letter, 2nd letter, etc.
for row in range(len(name)):
    # Left side of the N
    line = name[row]

    # Spaces between the left side and middle diagonal of the N
    for first_spaces in range(row - 1):
        line += " "

    # Middle diagonal of the N, careful not to print the first
    # or last letter an extra time.
    if 0 < row < len(name) - 1:
        line += name[row]

    # Spaces between the middle diagonal and right side of the N
    for second_spaces in range(len(name) - row - 2):
        line += " "

    # Right side of the N
    line += name[row]

    # We print one row at a time
    print line
