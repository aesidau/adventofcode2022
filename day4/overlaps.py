# print the number of pairs where one in a pair partially overlaps the other
import fileinput

def overlaps(a_start, a_end, b_start, b_end): # a overlaps b
  return (int(a_start) == int(b_start) or
          int(a_end) == int(b_end) or
          int(a_start) < int(b_start) and int(a_end) >= int(b_start) or
          int(a_end) > int(b_end) and int(a_start) <= int(b_end) or
          int(a_start) > int(b_start) and int(a_end) < int(b_end) or
          int(b_start) > int(a_start) and int(b_end) < int(a_end))

total = 0
for line in fileinput.input():
  ranges = line.split(',')
  range1 = ranges[0].split('-')
  range2 = ranges[1].split('-')
  if overlaps(range1[0], range1[1], range2[0], range2[1]):
    total += 1

print(total)
