# TODO: implement a 2-player mode
# TODO: Check if python does switch statements
# TODO: Re-implment this using an array!
# TODO: Re-implement this with an enumeration
# TODO: Add pictures

import random

actions = ["rock", "paper", "scissors"]

def game():
   user_input = raw_input(
       "Choose rock, paper, or scissors\n---> ")
   computer_input = random.choice(actions)
   print computer_input
   if user_input == computer_input:
       print "It's a tie"

   # All the computer rock combinations
   elif computer_input == "rock" and user_input == "paper":
       print "you win"
   elif computer_input == "rock" and user_input == "scissors":
       print "you lose"

   # All the computer paper combinations
   elif computer_input == "paper" and user_input == "scissors":
       print "you win"
   elif computer_input == "paper" and user_input == "rock":
       print "you lose"

   # All the computer scissors combinations
   elif computer_input == "scissors" and user_input == "paper":
       print "you lose"
   elif computer_input == "scissors" and user_input == "rock":
       print "you lose"

   else:
       print "please type in rock, paper, or scissors exactly"
   print "try again"
while True:
   game()
