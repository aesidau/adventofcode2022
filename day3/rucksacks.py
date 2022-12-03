# print the sum of the priorities of duplicate items in each rucksack (line)
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
for line in fileinput.input():
  part1 = line[0:int(len(line) / 2)]
  part2 = line[int(len(line) / 2):] # nb. will include the newline
  rucksack = {}
  duplicate = ' '
  for ch in part1:
    rucksack[ch] = 1
  for ch in part2:
    if ch in rucksack:
      duplicate = ch
      break
  total += priority(duplicate)

print(total)
