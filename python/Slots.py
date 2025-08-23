# In each round, the slot machine displays three random items. 

import random

symbols = ['🍒', ' 🍇', '🍉', '7️⃣']
results = random.choices(symbols, k=3)
print(*results, sep="|")

# If all of the list items in results are equal to '7️⃣', print "Jackpot! 💰".
# Else, print "Thanks for playing!".
if results[0] == '7️⃣' and results[1] == '7️⃣' and results[2] == '7️⃣':
  print("Jackpot! 💰")
else:
  print("Thanks for playing!")

