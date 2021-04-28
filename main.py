'''This is a game of 8-Ball where you can ask Yes/No Questions and get answers'''

alpha = True
while alpha == True:
 name = input("What is your name?: ")
 if name.isalpha() and name.strip():
  alpha = False
  beta = True
  while beta == True:
   question = input("Ask a (Yes/No) question: ")
   beta = False
 else:
  print("Your name has to be all letters and contain no spaces.")
answer = ""

import random

random_number = random.randint(1,9)


if random_number == 1:
  answer = "Magic 8-Ball says: Yes - definitely."

elif random_number == 2:
  answer = "Magic 8-Ball says: It is decidedly so"

elif random_number == 3:
 answer = "Magic 8-Ball says: Without a doubt."

elif random_number == 4:
 answer = "Magic 8-Ball says: Reply hazy, try again."

elif random_number == 5:
  answer = "Magic 8-Ball says: Ask again later."

elif random_number == 6:
  answer = "Magic 8-Ball says: Better not tell you now."

elif random_number == 7:
  answer = "Magic 8-Ball says: My sources say no."

elif random_number == 8:
  answer = "Magic 8-Ball says: Outlook not so good."

elif random_number == 9:
  answer = "Magic 8-Ball says: Very doubtful."

else:
  answer = "Error"

print(name + " asks: " + question)
print(answer)
