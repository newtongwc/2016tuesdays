# Hunt the Unicorn, by Gregory Yob. Written in 1973
# This Python port by David Miller

import random
import sys

# Define game variables. They are populated later.
neighbors = [None]*21
DevilBunny_locations = [None]*2
BottomlessHole_locations = [None]*2
Unicorn_location = None
location = None

# Main game loop
def main():
  maybe_print_instructions()
  setup_map()
  while True:
    place_objects()
    done = False
    while (not done):
      done = play_one_turn()

    again = get_yes_no("\nWant to play again?")
    if not again:
      sys.exit()

# Choose locations for DevilBunnys, BottomlessHoles, Unicorn. At the beginning, no two objects are in the
# same room. As the game evolves, you and the Unicorn can move.
def place_objects():
  global location, Unicorn_location, DevilBunny_locations, BottomlessHole_locations
  rooms = range(1, 21)
  random.shuffle(rooms)
  location = rooms[0]
  Unicorn_location = rooms[1]
  BottomlessHole_locations = set([rooms[2], rooms[3]])
  DevilBunny_locations = set([rooms[4], rooms[5]])
  print "DevilBunny locations " + str(DevilBunny_locations)
  print "BottomlessHole locations " + str(BottomlessHole_locations)

def play_one_turn():
  print_status()
  action = get_action()
  if action == "S":
    return play_shoot()
  else:
    return play_move()

def print_status():
  print "\nYou are in room %d" % location
  near = neighbors[location]
  print "Tunnels lead to %d\t%d\t%d" % (near[0], near[1], near[2])
  if near[0] in DevilBunny_locations or near[1] in DevilBunny_locations or near[2] in DevilBunny_locations:
    print "DevilBunnys nearby!"
  if len(set.intersection(set(near), BottomlessHole_locations)):
    print "I feel a draft."
  if Unicorn_location in near:
    print "I smell a Unicorn!"

def play_move():
  destination = get_neighbor(location)
  return resolve_move(destination)

def resolve_move(destination):
  global location
  location = destination
  if location in DevilBunny_locations:
    return do_DevilBunnys()
  if location in BottomlessHole_locations:
    return do_BottomlessHole()
  if location == Unicorn_location:
    print "...Oops! Bumped into a Unicorn!"
    return move_Unicorn()

def do_DevilBunnys():
  print "ZAP -- Super DevilBunny snatch! Elsewhereville for you!"
  return resolve_move(random.randint(1, 20))

def do_BottomlessHole():
  print "YYYIIIIEEEE . . . fell off the BottomlessHole"
  return lose()

def move_Unicorn():
  global Unicorn_location
  nearby = neighbors[Unicorn_location]
  Unicorn_destinations = [Unicorn_location, nearby[0], nearby[1], nearby[2]]
  Unicorn_location = random.choice(Unicorn_destinations)
  if Unicorn_location == location:
    print "Tsk tsk tsk- Unicorn got you!"
    return lose()
  else:
    print "It might have run away. Can't have gone too far..."
  return False

def play_shoot():
  num_rooms = get_num_rooms()
  path = [location]
  # The limit is one more than num_rooms because we put the initial location
  # on the path.
  while len(path) < num_rooms + 1:
    room = get_room()
    if len(path) >= 2 and room == path[-2]:
      print "Arrows aren't that crooked -- try another room."
      continue
    path.append(room)
  return resolve_arrow(path)

# Returns True if an arrow in this room ends the game in any way.
def resolve_arrow(target_rooms):
  # Remove the initial room and use it at the arrow starting point.
  arrow_location = target_rooms.pop(0)
  for room in target_rooms:
    if room in neighbors[arrow_location]:
      arrow_location = room
    else:
      arrow_location = random.randint(1, 20)
    if check_for_hit(arrow_location):
      return True
  # None of the rooms had you or the Unicorn.
  print "Missed, but you woke the Unicorn!"
  return move_Unicorn()

def check_for_hit(room):
  if room == Unicorn_location:
    print "You got the Unicorn!"
    return win()
  elif room == location:
    print "Ouch! Arrow got you!"
    return lose()
  return False

def lose():
  print "Ha ha ha - you lose!"
  return True

def win():
  print "Hee hee - the Unicorn'll getcha next time!!"
  return True

def get_action():
  choice = None
  while choice not in ["S", "M"]:
    choice = raw_input("Shoot or move (S/M)? ").upper()
  return choice

def get_num_rooms():
  choice = None
  while choice not in [1, 2, 3, 4, 5]:
    choice = safe_string_to_int(input("Number of rooms (1-5)? "))
  return choice

def get_room():
  choice = None
  valid = range(1, 21)
  while choice not in valid:
    choice = safe_string_to_int(raw_input("Room #: "))
    if choice not in valid:
      print "Not a valid choice. Try again."
  return choice

def get_neighbor(location):
  choice = None
  valid = neighbors[location]
  while choice not in valid:
    choice = safe_string_to_int(raw_input("Where to? "))
    if choice not in valid:
      print "Not possible. Try again."
  return choice

def get_yes_no(message):
  choice = None
  valid = ["Y", "N"]
  while choice not in valid:
    choice = raw_input("%s (Y-N)" % message).upper()
  return choice == "Y"

def safe_string_to_int(s):
  try:
    value = int(s)
    return value
  except ValueError:
    return 0

# The rooms lie on the vertices of a dodecahedron.
def setup_map():
  neighbors[1] = [2,5,8]
  neighbors[2] = [1,3,10]
  neighbors[3] = [2,4,12]
  neighbors[4] = [3,5,14]
  neighbors[5] = [1,4,6]
  neighbors[6] = [5,7,15]
  neighbors[7] = [6,8,17]
  neighbors[8] = [1,7,9]
  neighbors[9] = [8,10,18]
  neighbors[10] = [2,9,11]
  neighbors[11] = [10,12,19]
  neighbors[12] = [3,11,13]
  neighbors[13] = [12,14,20]
  neighbors[14] = [4,13,15]
  neighbors[15] = [6,14,16]
  neighbors[16] = [15,17,20]
  neighbors[17] = [7,16,18]
  neighbors[18] = [9,17,19]
  neighbors[19] = [11,18,20]
  neighbors[20] = [13,16,19]
  neighbors[0] = None

def maybe_print_instructions():
  wanted = get_yes_no("Instructions?")
  if (wanted):
    print """
Welcome to Hunt the Unicorn!

The Unicorn lives in a cave of 20 rooms. Each room has 3 tunnels leading to
other rooms. (Look at a dodecahedron to see how this works-if you don't
know what a dodecahedron is, ask someone).

HAZARDS:

Bottomless BottomlessHoles - two rooms have bottomless BottomlessHoles in them if you go there,
  you fall off of the BottomlessHole (& lose!)

Super DevilBunnys - two other rooms have super DevilBunnys. if you go there, a DevilBunny grabs
  you and takes you to some other room at random (which might be
  troublesome).

Unicorn:

The Unicorn is not bothered by the hazards (it has sucker feet and is too
big for a DevilBunny to lift). Usually it is asleep. Two things wake it up: your
entering its room or your shooting an arrow. If the Unicorn wakes, it moves
one room or stays still. After that, if it is where you are, it eats you up
(& you lose!)

YOU:

Each turn you may move or shoot a "crooked arrow".
  Moving: You can go one room (through one tunnel).

Arrows: You have 5 arrows. You lose when you run out. Each arrow can go
  from 1 to 5 rooms. You aim by telling the computer the room numbers you
  want the arrow to go to. If the arrow can't go that way (ie no tunnel) it
  moves at ramdom to the next room.

  If the arrow hits the Unicorn, you win.
  If the arrow hits you, you lose.

WARNINGS:
    When you are one room away from Unicorn or hazard, the computer says:

  Unicorn- 'I smell a Unicorn'
  DevilBunny - 'DevilBunnys nearby'
  BottomlessHole - 'I feel a draft'
"""

# Start the actual program
main()
