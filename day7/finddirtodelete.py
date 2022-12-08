# read in a filesystem and find directory to delete that would give 30,000,000 free space
import sys

# read in the files of the filesystem and their sizes
filesystem = {}
directory = []
while True:
  line = sys.stdin.readline().strip()
  if line == "\n" or line == "":
    break
  match line[0]:
    case '$': # command
      if line.startswith("$ cd "):
        newdir = line[5:]
        if newdir == "/":
          directory = []
        elif newdir == "..":
          directory.pop()
        else:
          directory.append(newdir)
    case 'd': # a directory listing
      pass
    case _: # a file listing
      parts = line.split()
      if len(directory) == 0:
        filename = "/" + parts[1]
      else:
        filename = "/" + "/".join(directory) + "/" + parts[1]
      filesystem[filename] = int(parts[0])

# calculate how large each directory is
dirsizes = {}
for file, size in filesystem.items():
  path = file.split("/")
  for pos in range(len(path)-1):
    directory = "/".join(path[0:pos+1])
    if directory in dirsizes:
      dirsizes[directory] += size
    else:
      dirsizes[directory] = size

# figure out how much free space we need
required = 30000000 - (70000000 - dirsizes[""])

# find the size of the smallest directory at least that large
minimum = dirsizes[""]
for directory, size in dirsizes.items():
  if size < minimum and size >= required:
    minimum = size

print(minimum)

