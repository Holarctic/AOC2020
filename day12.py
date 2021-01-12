from downloadInput import start
from parse import parse
day = 12
input=[]
file = "day%d/input.txt" % day
# file = "test.txt"
for line in open(file, "r").readlines():
  input.append(list(parse("{}{:d}", line)))


def part1(input):
  x,y=0,0
  direction = 0
  for instruction, value in input:
    if instruction == "N":
      y += value
    elif instruction == "S":
      y -= value
    elif instruction == "E":
      x += value
    elif instruction == "W":
      x -= value
    elif instruction == "L":
      direction += value 
      direction += 360
      direction %= 360
    elif instruction == "R":
      direction -= value
      direction += 360
      direction %= 360
    elif instruction == "F":
      if direction == 0:
        x += value
      elif direction == 90:
        y += value
      elif direction == 180:
        x -= value
      elif direction == 270:
        y -= value
  return abs(x) + abs(y)



def part2(input):
  x,y=0,0
  wx, wy = 10,1
  # direction = 0
  for instruction, value in input:
    if instruction == "N":
      wy += value
    elif instruction == "S":
      wy -= value
    elif instruction == "E":
      wx += value
    elif instruction == "W":
      wx -= value
    elif instruction == "L":
      if value == 90:
        wx,wy = -wy, wx
      elif value == 180:
        wx,wy = -wx,-wy
      elif value == 270:
        wx,wy =  wy,-wx
    elif instruction == "R":
      if value == 90:
        wx,wy =  wy,-wx
      elif value == 180:
        wx,wy = -wx,-wy
      elif value == 270:
        wx,wy =  -wy,wx
    elif instruction == "F":
      x += wx*value
      y += wy*value
    print(x,y)
  return abs(x) + abs(y)



def day12(input):
  print("Day 12 part1: ", part1(input))
  print("Day 12 part2: ", part2(input))

day12(input)