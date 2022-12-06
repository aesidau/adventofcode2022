# find the end of the marker (four different characters) in the data stream
import sys

# read in the data stream

def shift_buffer(buff):
  buff[0] = buff[1]
  buff[1] = buff[2]
  buff[2] = buff[3]

def all_different(buff):
  characters = [buff[0], buff[1], buff[2], buff[3]]
  characters.sort()
  return (characters[0] != characters[1] and
          characters[1] != characters[2] and
          characters[2] != characters[3])

stream = sys.stdin.readline()
buffer = {0: '0', 1: '0', 2: '0', 3: '0'}
for idx in range(len(stream)):
  shift_buffer(buffer)
  buffer[3] = stream[idx]
  if all_different(buffer) and idx > 2:
    break

print(idx + 1)
