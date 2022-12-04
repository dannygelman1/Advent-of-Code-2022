f = open("./advent1.txt", "r")

listNumbers = f.read().split("\n")
arrayMaxCalories = [float("-inf"), float("-inf"), float("-inf")]
sumCalories = 0
for number in listNumbers:
  if (number!=""):
    sumCalories += int(number)
  else:
    if sumCalories> min(arrayMaxCalories):
      index = arrayMaxCalories.index(min(arrayMaxCalories))
      arrayMaxCalories[index] = sumCalories
    sumCalories = 0
print("Part 1: ", max(arrayMaxCalories))
print("Part 2: ", sum(arrayMaxCalories))
