import random

num = random.randint(1,25)

print("Guess a number between 1 and 25 (both included)")

guess = 0
tries = 0

while guess != num :
    guess = int (input ())
    if guess != num :
        print("Wrong guess Try Again")
    else:
        break
    tries += 1
if tries < 5:
    print("Did you use hack,that was fast")
elif tries < 10 and tries >=5:
    print("You are quite the guesser")
else:
    print("Committed,now that took a while")