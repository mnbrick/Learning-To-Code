# Score each question
# Print out a total score for each house
# Print the house with the most points

Gryffindor = 0
Ravenclaw = 0
Hufflepuff = 0
Slytherin = 0

print("Do you like Dawn or Dusk?")
a1 = int(input("1. Dawn; 2. Dusk: "))
if a1 == 1:
    Gryffindor += 1
    Ravenclaw += 1
elif a1 == 2:
    Hufflepuff += 1
    Slytherin += 1
else:
    print("WRONG INPUT")

print("When I’m dead, I want people to remember me as:")
a2 = int(input("1. The Good; 2. The Great; 3. The Wise; 4. The Bold: "))
if a2 == 1:
    Hufflepuff += 2
elif a2 == 2:
    Slytherin += 2
elif a2 == 3:
    Ravenclaw += 2
elif a2 == 4:
    Gryffindor += 2
else:
    print("WRONG INPUT")

print("Which kind of instrument most pleases your ear?")
a3 = int(input("1. The Violin; 2. The Trumpet; 3. The Piano; 4. The Drum: "))
if a3 == 1:
    Slytherin += 4
elif a3 == 2:
    Hufflepuff += 4
elif a3 == 3:
    Ravenclaw += 4
elif a3 == 4:
    Gryffindor += 4
else:
    print("WRONG INPUT")

print("Gryffindor's final score:", Gryffindor)
print("Ravenclaw's final score:", Ravenclaw)
print("Hufflepuff's final score:", Hufflepuff)
print("Slytherin's final score:", Slytherin)

if Gryffindor > Ravenclaw and Gryffindor > Hufflepuff and Gryffindor > Slytherin:
    print("Gryffindor")
elif Ravenclaw > Gryffindor and Ravenclaw > Hufflepuff and Ravenclaw > Slytherin:
    print("Ravenclaw")
elif Hufflepuff > Gryffindor and Hufflepuff > Ravenclaw and Hufflepuff > Slytherin:
    print("Hufflepuff")
elif Slytherin > Gryffindor and Slytherin > Ravenclaw and Slytherin > Hufflepuff:
    print("Slytherin")
else:
    print("Voldemort has infiltrated the Sorting Hat!!!!")
