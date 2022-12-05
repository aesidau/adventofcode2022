# print the number of pairs where one in a pair contains the other
import fileinput

def contains(a_start, a_end, b_start, b_end): # a contains b
  return int(a_start) <= int(b_start) and int(a_end) >= int(b_end)

def contains_eitherway(a_start, a_end, b_start, b_end):
  return contains(a_start, a_end, b_start, b_end) or contains(b_start, b_end, a_start, a_end)

total = 0
for line in fileinput.input():
  ranges = line.split(',')
  range1 = ranges[0].split('-')
  range2 = ranges[1].split('-')
  if contains_eitherway(range1[0], range1[1], range2[0], range2[1]):
    total += 1

print(total)
