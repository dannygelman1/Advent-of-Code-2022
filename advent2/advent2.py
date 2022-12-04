f = open("./advent2.txt", "r")
listRounds = f.read().split("\n")

def winLooseOrDraw(player1, player2):
  increm = player1+1
  if (player1==player2):
    return 3
  if (increm>3):
    if ((increm)%3==player2):
      return 6
    else:
      return 0
  else:
    if (increm==player2):
      return 6
    else:
      return 0

def convertLetterToNumber(letter):
  if (letter=="A" or letter=="X"):
    return 1
  if (letter=="B" or letter=="Y"):
    return 2
  if (letter=="C" or letter=="Z"):
    return 3

def choiceBasedOnOutcome(player1, outcome):
  if (outcome==3):
    return player1
  if (outcome==0):
    if (player1>1):
      return player1-1
    else:
      return 3
  if (outcome==6):
    if (player1<3):
      return player1+1
    else:
      return 1

def convertLetterToOutcome(letter):
  if (letter=="X"):
    return 0
  if (letter=="Y"):
    return 3
  if (letter=="Z"):
    return 6

score1 = 0
listRounds.pop()
for turn in listRounds:
  player1 = convertLetterToNumber(turn[0])
  player2 = convertLetterToNumber(turn[2])
  score1 += player2 + winLooseOrDraw(player1, player2)

score2 = 0
for turn in listRounds:
  player1 = convertLetterToNumber(turn[0])
  outcome = convertLetterToOutcome(turn[2])
  score2 += outcome + choiceBasedOnOutcome(player1, outcome)

print("Part 1: ", score1)
print("Part 2: ", score2)
