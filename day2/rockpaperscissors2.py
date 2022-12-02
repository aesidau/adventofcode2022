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
  'C': 'X'  #rock beats scissors
}

draws = {
  'A': 'X', #rock
  'B': 'Y', #paper
  'C': 'Z'  #scissors
}

loss = {
  'A': 'Z', #scissors loses to rock
  'B': 'X', #rock loses to paper
  'C': 'Y'  #paper loses to scissors
}

total = 0
for line in fileinput.input():
  moves = line.split()
  match moves[1]:
    case 'X': #to lose
      play = loss[moves[0]]
      score = 0
    case 'Y': #to draw
      play = draws[moves[0]]
      score = 3
    case 'Z': #to win
      play = beats[moves[0]]
      score = 6
  score += shape_score[play]
  total += score

print(total)
