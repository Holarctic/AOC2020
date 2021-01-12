from downloadInput import start
from parse import parse
day = 14
input=[]
file = "day%d/input.txt" % day
# file = "test.txt"

def part1(input):
  def masked(mask, val):
    val = list(format(val, "036b"))
    for i in range(len(mask)):
      if mask[i] != 'X':
        val[i] = mask[i]
    return int("".join(val),2)
    
  memory = dict()
  mask = ""
  for line in open(file, "r").readlines():
    if line[1] == "a":
      mask = parse("mask = {}", line)[0]
    while line[1] == "e":
      mem, val = parse("mem[{:d}] = {:d}", line)
      memory[mem] = masked(mask, val)
      break
  return sum(memory.values())

def part2(input):
  def masked(mask, val):
    val = list(format(val, "036b"))
    pos = []
    for i in range(len(mask)):
      if mask[i] == "1":
        val[i]= mask[i]
      elif mask[i] == "X":
        pos.append(i)
    rez = []
    for i in range(2**len(pos)):
      target = list(format(i, "0%db"%len(pos)))
      for x,y in zip(pos,target):
        val[x] = y
      rez.append(int("".join(val),2))
    return rez
    
  memory = dict()
  mask = ""
  for line in open(file, "r").readlines():
    if line[1] == "a":
      mask = parse("mask = {}", line)[0]
    while line[1] == "e":
      mem, val = parse("mem[{:d}] = {:d}", line)
      for x in masked(mask, mem):
        memory[x] = val 
      break
  return sum(memory.values())

def day14(input):
  print("Day 14 part1: ", part1(input))
  print("Day 14 part2: ", part2(input))

day14(input)