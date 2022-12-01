# print the total of the highest three sums of groups of numbers separated by a blank line
import fileinput

sums = []
count = 0
for line in fileinput.input():
  if line == '\n' or len(line) == 0:
    sums.append(count)
    count = 0
  else:
    count += int(line)
if count > 0:
  sums.append(count)
sums.sort(reverse=True)
total = 0
for i in range(min(3,len(sums))):
  total += sums[i]
print(total)
