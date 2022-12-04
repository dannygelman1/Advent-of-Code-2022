f = open("./advent1.txt", "r")

calories = f.read().split("\n")
maxCalories = [float("-inf"), float("-inf"), float("-inf")]
sumCalories = 0
for number in calories:
  if (number!=""):
    sumCalories += int(number)
  else:
    if sumCalories> min(maxCalories):
      index = maxCalories.index(min(maxCalories))
      maxCalories[index] = sumCalories
    sumCalories = 0
print("Part 1: ", max(maxCalories))
print("Part 2: ", sum(maxCalories))
