from collections import defaultdict
import copy
from downloadInput import start
from parse import parse
day = 11

# seats = {"#":1, "L":0, ".":0}
file = "day%d/input.txt" % day
# file = "test.txt"
def data (file):
  # default = "."
  input=[[]]
  for i, line in enumerate(open(file, "r").readlines()):
    for char in line:
      if char is not "\n":
        input[i].append(char)
    input.append([])
  input.pop()
  return input

def checkAdjecent(input, coords):
  counter = 0
  for i in [-1,0,1]:
    if 0 <= coords[0]+i < len(input):
      for j in [-1,0,1]:
        if 0 <= coords[1]+j < len(input[i]):
          if i == 0 and j == 0:
            continue
        
          try:
            if input[coords[0]+i][coords[1]+j] == "#":
              counter += 1
          except:
            if coords[1]==9:
              print(coords, (i,j))
  return counter

def prt (input):
  for line in input:
    print("".join(line))

def part1(input):
  temp = copy.deepcopy(input)
  flag = False
  for x in range(len(input)):
    for y in range(len(input[x])):
      if input[x][y] == "L" and checkAdjecent(input, (x,y))==0:
        temp[x][y]="#"
        flag=True
      if input[x][y] == "#":
        if checkAdjecent(input, (x,y))>=4:
          temp[x][y]="L"
          flag=True
  if not flag:
    # prt(input)
    counter =0
    for line in input:
      for x in line:
        if x == "#":
          counter += 1
    return counter
  else:
    return part1(temp)


def checkLong(input, coords):
  def checkRow(input, coords):
    counter = 0
    tmp = [x for x in input[coords[0]][:coords[1]] if x != "."]
    if tmp and tmp[-1]=="#":
      counter += 1
    for x in input[coords[0]][coords[1]+1:]:
      if x == "L":
        return counter
      if x == "#":
        return counter+1
    return counter
  def checkDiagonal1(input, coords):
    counter = 0
    # tmp=[]
    x = max((len(input), len(input[0])))
    for i in range(-1, -x-1, -1):
      if 0 <= coords[0] + i <len(input):
        if 0 <= coords[1] + i < len(input[0]):
          if input[coords[0]+i][coords[1]+i] == "L":
            break
          if input[coords[0]+i][coords[1]+i] == "#":
            counter += 1
            break
    for i in range (1, x):
      if 0 <= coords[0] + i <len(input):
        if 0 <= coords[1] + i < len(input[0]):
          if input[coords[0]+i][coords[1]+i] == "L":
            break
          if input[coords[0]+i][coords[1]+i] == "#":
            counter += 1
            break
    return counter
  def checkDiagonal2(input, coords):
    counter = 0
    # tmp=[]
    x = max((len(input), len(input[0])))
    for i in range(-1, -x-1, -1):
      if 0 <= coords[0] + i <len(input):
        if 0 <= coords[1] - i < len(input[0]):
          if input[coords[0]+i][coords[1]-i] == "L":
            break
          if input[coords[0]+i][coords[1]-i] == "#":
            counter += 1
            break
    for i in range (1, x):
      if 0 <= coords[0] + i <len(input):
        if 0 <= coords[1] - i < len(input[0]):
          if input[coords[0]+i][coords[1]-i] == "L":
            break
          if input[coords[0]+i][coords[1]-i] == "#":
            counter += 1
            break
    return counter
  # print(checkRow(input, coords))
  # print(checkRow(list(map(list, zip(*input))), (coords[1], coords[0])))
  # print(checkDiagonal1(input, coords))
  # print(checkDiagonal2(input, coords))
  # print()
  return checkRow(input, coords) + checkRow(list(map(list, zip(*input))), (coords[1], coords[0])) + checkDiagonal1(input, coords) + checkDiagonal2(input, coords)

def part2(input):
  temp = copy.deepcopy(input)
  flag = False
  for x in range(len(input)):
    for y in range(len(input[x])):
      if input[x][y] == "L" and checkLong(input, (x,y))==0:
        temp[x][y]="#"
        flag=True
      if input[x][y] == "#":
        if checkLong(input, (x,y))>=5:
          temp[x][y]="L"
          flag=True
  if not flag:
    # prt(input)
    counter =0
    for line in input:
      for x in line:
        if x == "#":
          counter += 1
    return counter
  else:
    # print("got here")
    return part2(temp)



def day11(input):
  input = data(file)
  # print("Part 1: ", part1(input))
  print("Part 2: ", part2(input))
day11(input)