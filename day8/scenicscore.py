# calculate maximum scenic score of any tree in the grid
import sys

def scoreup(rowidx, colidx):
  height = int(treegrid[rowidx][colidx])
  score = 0
  while rowidx >= 1:
    rowidx -= 1
    score += 1
    if int(treegrid[rowidx][colidx]) >= height:
      break
  return score

def scoredown(rowidx, colidx):
  height = int(treegrid[rowidx][colidx])
  score = 0
  while rowidx < rows - 1:
    rowidx += 1
    score += 1
    if int(treegrid[rowidx][colidx]) >= height:
      break
  return score

def scoreleft(rowidx, colidx):
  height = int(treegrid[rowidx][colidx])
  score = 0
  while colidx >= 1:
    colidx -= 1
    score += 1
    if int(treegrid[rowidx][colidx]) >= height:
      break
  return score

def scoreright(rowidx, colidx):
  height = int(treegrid[rowidx][colidx])
  score = 0
  while colidx < cols - 1:
    colidx += 1
    score += 1
    if int(treegrid[rowidx][colidx]) >= height:
      break
  return score


# read in a map of tree heights and initialise the visible map
treegrid = []
while True:
  line = sys.stdin.readline().strip()
  if line == "\n" or line == "":
    break
  treegrid.append(line)

rows = len(treegrid)
cols = len(treegrid[0])

# find the maximum score
maxscore = 0
for rowidx in range(rows):
  for colidx in range(cols):
    score = (scoreup(rowidx, colidx) * scoredown(rowidx, colidx) *
             scoreright(rowidx, colidx) * scoreleft(rowidx, colidx))
    if score > maxscore:
      maxscore = score

print(maxscore)

