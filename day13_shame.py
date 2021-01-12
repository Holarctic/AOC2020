from downloadInput import start
from parse import parse
import time
day = 13
input=[]
file = "day%d/input.txt" % day
# file = "test.txt"
lines = open(file, "r").readlines()
t = int(lines[0])
input = [int(x) if x!= "x" else "x" for x in lines[1].split(",")]
input = [t, input]

def part1(input):
  minTime = input[1][0]
  for x in input[1]:
    if x != "x":
      if (x-input[0]%x) < (minTime - input[0]%minTime):
        minTime = x
  return minTime * (minTime - input[0]%minTime)



def part2(input):
  # input = input[1]
  flag = True
  input = [(x, i) for i,x in enumerate(input[1]) if x!="x"] 
  # start = input[0][0]
  t = input[0][0]
  start = time.time()
  while flag:
    tFlag = False
    for x, i in input:
      # print(x, i)
      if (t+i)%x != 0:
        t += input[0][0]
        tFlag = True
        break
    flag = tFlag
    if time.time() - start > 60:
      return t/input[0][0]
  return t

def day13(input):
  print("Day 13 part1: ", part1(input))
  print("Day 13 part2: ", part2(input))

day13(input)