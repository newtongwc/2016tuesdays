def googleFeud():
  import random
  
  score = 0
  class Question:
    def __init__(self, query, best, worse):
        self.query = query
        self.best = best
        self.worse = worse
  
  questions = [
    Question("*There is a law against", "cannibalism","flag burning"),
    Question("The Beatles are", "half alive and half dead", "dead"),
    Question("The atomic number of nitrogen is", "7", "2"),
    Question("SpongeBob's best friend is", "Patrick", "Squidward"),
    Question("Luna Lovegood is a", "Ravenclaw", "Gryffindor"),
    Question("True or false: cannibals find volunteer victims on the internet", "true", "false"),
    Question("The Newton North High School mascot is the", "tiger", "lion"),
    Question("True or false: bulldogs need to have their face folds cleaned to avoid infection.", "true", "false")
    ]
  
  print "Let's play Google Feud!"
  print "Your score is 0."
  while True:
    question = random.choice(questions)  
    print "Guess the more likely completion.\n"
    print "query: %s __________" % question.query
    if random.choice([True, False]):
      answerA = question.best
      answerB = question.worse
      correct = "A"
    else:
      answerA = question.worse
      answerB = question.best
      correct = "B"
  
    print "(A) %s" % answerA
    print "(B) %s" % answerB
    response = raw_input("\n--->")
    if response != "A" and response != "B":
      print "\nYou must choose A or B. Try again with this question."
      continue
    
    if response == correct:
      result = "Correct!"
      score = score + 1
      displayScore "Your score is %i" %score
    else:
      result = "Wrong! Game over!"
      break
  
    print "%s! It's (%s) %s.\n" % (result, correct, question.best, displayScore)
    
    googleFeud()
