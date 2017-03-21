import random
def wordScramble():  
  print "Welcome to Word Scramble (fruit theme)!\n\n"
  print "Try unscrambling these letters to make an english word.\n"
  print "You will gain a point for each correct answer until you get an answer wrong."
  
  score = 0
  
  #List of fruits to unscramble.
  words = ["apple", "banana", "pear", "apricot", "orange", "peach", "mango", "kiwi", "kumquat", "lemon", "lime", "grapefruit"]
  
  
  while True:
    index = random.randint(0, len(words) - 1)
    letters = list(words[index])
    random.shuffle(letters)
    scramble = ''.join(letters)
    
    print "Scrambled: %s" % scramble
    guess = raw_input("What word is this? ")
    guess = str.lower(guess)
    if guess == words[index]:
      print "\nYou are correct!\n"
      score = score + 1
      print "\nYour score is %i\n" % score
      list.remove(words[index])
    else:
      print "\nNo, the word was %s\n" % word
      print"Game over. You lose!"
      print "\nYour score was %i\n" % score
      break
wordScramble()
again = True
while again:
  print "Do you want to play again?"
  guess = raw_input("If you want to play again, type yes.")  
  guess = str.lower(guess)
  if guess == "yes":
    wordScramble()
  else:
    again == False
