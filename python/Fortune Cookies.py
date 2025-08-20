# gives the user random fortunes
# use random.randint() to randomize

import random

def fortune():
  possibility = random.randint(1,8)
  if possibility == 1:
    print("Don't pursue happiness – create it.")
  elif possibility == 2:
    print('All things are difficult before they are easy.')
  elif possibility == 3:
      print('The early bird gets the worm, but the second mouse gets the cheese.')
  elif possibility == 4:
      print('Someone in your life needs a letter from you.')
  elif possibility == 5:
    print("Don't just think. Act!")
  elif possibility == 6:
    print("Your heart will skip a beat.")
  elif possibility == 7:
    print("The fortune you search for is in another cookie.")
  else:
    print("Help! I'm being held prisoner in a Chinese bakery!")

fortune ()
fortune ()
fortune ()