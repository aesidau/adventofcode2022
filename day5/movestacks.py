# move the crates from the given stacks with the given operations
import sys

# read in the starting arrangement of the stacks
stacks = {}
while True:
  line = sys.stdin.readline()
  if line == "\n" or line == "":
    break
  if '[' in line:
    numstacks = int(len(line)/4)
    for stackidx in range(numstacks):
      crate = line[stackidx*4:(stackidx+1)*4].strip("[] \n")
      if crate != "":
        if stackidx not in stacks:
          stacks[stackidx] = []
        stacks[stackidx].append(crate)
  else:
    # we're on the final line of the table, reverse the stacks
    for stackidx in range(len(stacks)):
      stacks[stackidx].reverse()

# read in the instructions
while True:
  line = sys.stdin.readline()
  if line == "":
    break
  operation = line.split()
  numcrates = int(operation[1])
  source = int(operation[3])-1
  destination = int(operation[5])-1
  for numops in range(numcrates):
    crate = stacks[source].pop()
    stacks[destination].append(crate)

# print out top of each stack
for stackidx in range(len(stacks)):
  crate = stacks[stackidx].pop()
  print(crate, end="")
print()
