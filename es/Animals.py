animals = []
animalLength = []
greatest_animal_length = 0
while True:
    animal = raw_input("Enter an animal!")
    animals.append(animal)
    animalLen = len(animal)
    animalLength.append(animalLen)
    for i in animals:
        print i
    if len(animal) > greatest_animal_length:
         greatest_animal_length = len(animal)
    print "The longest animal so far has been %i characters long"%greatest_animal_length
    #if len(animals) == greatest_animal_length:
      #  print "The longest animals have been %s"
