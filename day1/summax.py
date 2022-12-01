# print the maximum of the sum of groups of numbers separated by a blank line
import fileinput

max_count = 0
count = 0
for line in fileinput.input():
  if line == '\n' or len(line) == 0:
    if count > max_count:
      max_count = count
    count = 0
  else:
    count += int(line)
if count > max_count:
  max_count = count
print(max_count)
