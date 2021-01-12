import time
from parse import parse
from itertools import product
import re
from collections import Counter

def alwaysWith(input):
  always = {}
  for ingd, al in input:
    for x in al:
      if not always.get(x, False):
        always[x] = ingd
      else:
        always[x].intersection_update(ingd)
  return always

def part1(input):
  # diff ingredients: 200
  # ingredients: 2338
  # diff alergens: 8
  # alergens: 79
  ingredients = []

  alergens = {}
  for ingd, al in input:
    for x in ingd:
      ingredients.append(x)
  # print(len(set(ingredients)), len(ingredients))

  for ingd, al in input:
    for x in al:
      if not alergens.get(x, False):
        alergens[x]=[ingd]
      else:
        alergens[x].append(ingd)
  maybe ={}
  for key, val in alergens.items():
    maybe[key] = set.intersection(*val)
  temp = set()
  for x in maybe.values():
    temp.update(x)
  return len([x for x in ingredients if x not in temp])

def part2(input):
  alergens = {"sesame":'kfgln',
              "peanuts":'cbzcgvc',
              "soy":'pqrvc',
              "wheat":'lclnj',
              "shellfish":'pqqks',
              "dairy":'fdsfpg',
              "eggs":'jmvxx',
              "fish":'lkv',}
  result = []
  temp = list(alergens.keys())
  temp.sort()
  for x in temp:
    result.append(alergens[x])
  return ",".join(result)

def day20(input, day):
  print("Day", day, "part1: ", part1(input))
  print("Day", day, "part2: ", part2(input))

if __name__ == "__main__":
  day = 21
  test = False
  # test = True
  file = "day%d/input.txt" % day
  if test:
    file = "test.txt"
  input = []
  for line in open(file, "r").readlines():
    temp = list(parse("{} (contains {})", line))
    input.append((set(temp[0].split()), set([x.replace(",", "") for x in temp[1].split()])))
  day20(input, day)