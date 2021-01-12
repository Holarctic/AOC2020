import time
from parse import parse

def part1(input):
  def inRanges(num, ranges):
    for i in range(0, len(ranges), 2):
      if ranges[i] <= num <= ranges[i+1]:
        return True
    return False
  ranges=[]
  for x in input[0]:
    ranges += x[1:]
  rez = 0
  pop = []
  for i, ticket in enumerate(input[2]):
    for val in ticket:
      if not inRanges(val, ranges):
        rez += val
        if i not in pop:
          pop.append(i)
  # print(len(pop), len(input[2]))
  for i in reversed(pop):
    input[2].pop(i)
  return rez, input


def part2(input):
  def condition(ticket, field):
    for x in ticket:
      for i in range(0, len(field), 2):
        if not (field[0] <= x <= field[1] or field[2] <= x <= field[3]):
          return False
    return True
  
  nearbyTickets = list(map(list, zip(*input[2])))
  fields = [(x[0], x[1:]) for x in input[0]]
  fieldsOrdered = []

  for ticket in nearbyTickets:
    temp = []
    for field in fields:
      if condition(ticket, field[1]):
        temp.append(field[0])
    fieldsOrdered.append(temp)
  
  found = [x[0] for x in fieldsOrdered if len(x)==1]
  for p in range(20):
    for i in range(len(fieldsOrdered)):
      if len(fieldsOrdered[i]) != 1:
        fieldsOrdered[i] = [x for x in fieldsOrdered[i] if x not in found]
      if len(fieldsOrdered[i])==1:
        found.append(fieldsOrdered[i][0])
  rez = 1
  for i, x in enumerate(fieldsOrdered):
    if "departure" in x[0]:
      rez *= input[1][i]
  return rez

def day16(input, day):
  rez, input = part1(input)
  print("Day", day, "part1: ", rez)
  start = time.time()
  print("Day", day, "part2: ", part2(input))
  # print(time.time()-start)

if __name__ == "__main__":
  from nrby import *
  day = 16
  test = False
  # test = True
  input=[]
  file = "day%d/input.txt" % day
  if test:
    file = "test.txt"
  myTicket = [113,197,59,167,151,107,79,73,109,157,199,193,83,53,89,71,149,61,67,163]
  
  input = [[]]
  for line in open(file, "r").readlines():
    input[0].append(list(parse("{}: {:d}-{:d} or {:d}-{:d}", line)))

  if test:
    input.append([11,12,13])
    input.append([[3,9,18],[15,1,5],[5,14,9]])
  else:
    input.append(myTicket)
    input.append(nearbyTickets)

  # print(input[0])
  day16(input, day)