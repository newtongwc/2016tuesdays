import time
name = raw_input("Please enter your name ---> ")
number = input("Please enter how many N's you want the computer to make your name into ---> ")
# Put name in all caps.
name = name.upper()
print "Look, I am making your name into several N's!"

# Loop over all the letters in the name. A range based for loop keeps
# track of whether we're on the first letter, 2nd letter, etc.
for i in range (0, number):
  print " "
  for row in range(len(name)):
     # Left side of the N
     line = name[row]
     time.sleep(1)
     # Spaces between the left side and middle diagonal of the N
     for first_spaces in range(row - 1):
         line += " "
     # Middle diagonal of the N, careful not to print the first
     # or last letter an extra time.
     time.sleep(3)
     if 0 < row < len(name) - 1:
         line += name[row]
     # Spaces between the middle diagonal and right side of the N
     time.sleep(1)
     for second_spaces in range(len(name) - row - 2):
         line += " "
     # Right side of the N
     line += name[row]
     # We print one row at a time
     print line
     
     
