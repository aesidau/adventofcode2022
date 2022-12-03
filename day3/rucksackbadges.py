# print the sum of the priorities of items duplicated across each three lines
import fileinput

def priority(x):
  if x >= 'a' and x <= 'z':
    return ord(x) - ord('a') + 1
  if x >= 'A' and x <= 'Z':
    return ord(x) - ord('A') + 27
  print("error with finding priority of", x)

loss = {
  'A': 'Z', #scissors loses to rock
  'B': 'X', #rock loses to paper
  'C': 'Y'  #paper loses to scissors
}

total = 0
badgeset = {}
for line in fileinput.input():
  rucksack = {}
  for ch in line:
    rucksack[ch] = 1
  for item in rucksack:
    if item in badgeset:
      badgeset[item] += 1
      if badgeset[item] == 3:
        total += priority(item)
        badgeset = {}
        break
    else:
      badgeset[item] = 1

print(total)
