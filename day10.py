from downloadInput import start
from parse import parse
day = 10
input=[]
file = "day%d/input.txt" % day
for line in open(file, "r").readlines():
  input.append(parse("{:d}", line)[0])

test = [16, 10, 15, 5, 1, 11, 7, 19, 6, 12, 4]
test2 = [28, 33, 18, 42, 31, 14, 46, 20, 48, 47, 24, 23, 49, 45, 19, 38, 39, 11, 1, 32, 25, 35, 8, 17, 7, 9, 4, 2, 34, 10, 3]
# print(len(input))

def choices(input, num):
  return [x for x in input if 0<x-num<=3]

def day10p1(input):
  input = sorted(input)
  lastAdapter = 0
  counter1, counter3 = 0, 1
  choice = choices(input, lastAdapter)
  while choice:
    if choice[0] - lastAdapter == 1:
      counter1 += 1
    elif choice[0] - lastAdapter == 3:
      counter3 += 1
    lastAdapter = choice[0]
    choice = choices(input, lastAdapter)
  print(counter1, counter3, counter1 * counter3)


def backtrack(input, num, calculated):
  if num == calculated[0]:
    return calculated[1]
  combs=0 
  for choice in choices(input, num):
    if choice == calculated[0]:
      return combs + calculated[1]
    else:
      combs += backtrack(input, choice, calculated) 
  return combs

def day10p2(input):
  input = sorted(input)
  temp = [input[i] for i in range(len(input)-1) if input[i+1]-input[i] == 3]
  combs = (input[-1], 1)
  for i in reversed(temp):
    combs = (i, backtrack(input, i, combs))
  print(backtrack(input, 0, combs))

day10p2(input)