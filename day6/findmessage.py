# find the end of the marker (14 different characters) in the data stream
import sys

# read in the data stream

def shift_buffer(buff):
  for idx in range(len(buff)-1):
    buff[idx] = buff[idx+1]

def all_different(buff):
  # convert the buff dictionary into the characters list
  characters = []
  for idx in range(len(buff)):
    characters.append(buff[idx])
  # make sure all the characters are sorted in order
  characters.sort()
  # now need check only if any adjacent characters are the same
  for idx in range(len(characters)-1):
    if characters[idx] == characters[idx+1]:
      return False
  return True

stream = sys.stdin.readline()
# initialise a sliding window of the desired size called buffer
buffer = {}
for idx in range(14):
  buffer[idx] = '0'
for idx in range(len(stream)):
  # slide the window and put the new character in the free place
  shift_buffer(buffer)
  buffer[len(buffer)-1] = stream[idx]
  # check if we've found the marker
  if all_different(buffer) and idx >= (len(buffer)-1):
    break

print(idx + 1)
