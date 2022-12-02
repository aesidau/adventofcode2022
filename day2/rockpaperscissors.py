# print the score from playing rock paper scissors according to the given play
import fileinput

shape_score = {
  'X': 1, #rock
  'Y': 2, #paper
  'Z': 3  #scissors
}

beats = {
  'A': 'Y', #paper beats rock
  'B': 'Z', #scissors beats paper
  'C': 'X' #rock beats scissors
}

draws = {
  'A': 'X', #rock
  'B': 'Y', #paper
  'C': 'Z' #scissors
}

total = 0
for line in fileinput.input():
  moves = line.split()
  score = shape_score[moves[1]]
  if moves[1] == draws[moves[0]]:
    score += 3 #draw
  elif moves[1] == beats[moves[0]]:
    score += 6 #win
  total += score

print(total)
