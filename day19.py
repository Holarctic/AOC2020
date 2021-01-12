import time
from parse import parse
from itertools import product

def part1(input):
  def valid(string, rules, rule):
    #[35,35]
    def testSimple(string, rules, rule):
      temp, val = valid(string, rules, rules[rule[0]])
      if val and temp:
        return valid(temp, rules, rules[rule[1]])
      else:
        return string, False

    if type(rules[rule])==type(""):
      return string[1:], string[0] == rules[rule]
    if type(rules[rule][0])==type(0):
      return testSimple(string, rules, rules[rule])
    if type(rules[rule][0])==type([]):
      for x in rules[rule]:
        temp, val = testSimple(string, rules, x)
        if val:
          return temp, val

        return string, False

  print(input[1][1])
  return "pog"

def part2(input):
  return "not pog"

def day19(input, day):
  print("Day", day, "part1: ", part1(input))
  print("Day", day, "part2: ", part2(input))

if __name__ == "__main__":
  from day19.rules import rules
  day = 19
  test = False
  test = True
  file = "day%d/input.txt" % day
  if test:
    file = "test.txt"
  input = [rules]
  input.append([line.strip() for line in open(file, "r").readlines()])
  day19(input, day)