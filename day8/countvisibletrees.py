# count the number of trees visible from any of four directions
import sys

# read in a map of tree heights and initialise the visible map
treegrid = []
visible = []
while True:
  line = sys.stdin.readline().strip()
  if line == "\n" or line == "":
    break
  treegrid.append(line)
  visibleline = []
  for idx in range(len(line)):
    visibleline.append(False)
  visible.append(visibleline)

height = len(treegrid)
width = len(treegrid[0])

# mark those visible from the top
maxheights = []
for colidx in range(width):
  maxheights.append(-1)
for rowidx in range(0,height-1):
  for colidx in range(width):
    thisheight = int(treegrid[rowidx][colidx])
    if thisheight > maxheights[colidx]:
      visible[rowidx][colidx] = True
      maxheights[colidx] = thisheight

# mark those visible from the bottom
maxheights = []
for colidx in range(width):
  maxheights.append(-1)
for rowidx in range(height-1,0,-1):
  for colidx in range(width):
    thisheight = int(treegrid[rowidx][colidx])
    if thisheight > maxheights[colidx]:
      visible[rowidx][colidx] = True
      maxheights[colidx] = thisheight

# mark those visible from the left
maxheights = []
for rowidx in range(height):
  maxheights.append(-1)
for colidx in range(0,width-1):
  for rowidx in range(height):
    thisheight = int(treegrid[rowidx][colidx])
    if thisheight > maxheights[rowidx]:
      visible[rowidx][colidx] = True
      maxheights[rowidx] = thisheight

# mark those visible from the right
maxheights = []
for rowidx in range(height):
  maxheights.append(-1)
for colidx in range(width-1,0,-1):
  for rowidx in range(height):
    thisheight = int(treegrid[rowidx][colidx])
    if thisheight > maxheights[rowidx]:
      visible[rowidx][colidx] = True
      maxheights[rowidx] = thisheight

# count the remaining visible trees
total = 0
for row in visible:
  total += row.count(True)

# print the visible trees
#for rowidx in range(height):
#  for colidx in range(width):
#    print ("*", end="") if visible[rowidx][colidx] else print(" ", end="")
#  print()

print(total)

