import time
from parse import parse

def part1(input):
  def evaluate(input):
    if input[-1] == "(":
      input.pop()
      rez = evaluate(input)
      if input[-1] == ")":
        input.pop()
    else:
      rez = int(input.pop())  
    while len(input)>1 and input[-1] != ")":
      if input[-1] == "+":
        input.pop()
        if input[-1] == "(":
          input.pop()
          rez += evaluate(input)
          if input[-1] == ")":
            input.pop()
        else:
          rez += int(input.pop())
      elif input[-1] == "*":
        input.pop()
        if input[-1] == "(":
          input.pop()
          rez *= evaluate(input)
          if input[-1] == ")":
            input.pop()
        else:
          rez *= int(input.pop())
    return rez
  
  sum = 0
  for x in input:
    sum += evaluate(x)
  return sum

def part2(input):
 return "pog"

def day18(input, day):
  print("Day", day, "part1: ", part1(input))
  print("Day", day, "part2: ", part2(input))

if __name__ == "__main__":
  day = 18
  test = False
  # test = True
  input=[]
  file = "day%d/input.txt" % day
  if test:
    file = "test.txt"

  input = [list(reversed(line.split())) for line in open(file, "r").readlines()]
  # print(input[0])
  day18(input, day)