import time
from parse import parse
from itertools import product
import re
def rotate(piece):
  return ["".join(x) for x in list(map(list, zip(*piece)))]
def edges(piece):
  temp = rotate(piece)
  edge = [piece[0], piece[-1], temp[0], temp[-1]]
  rotated = [x[::-1] for x in edge]
  return list(zip(edge, rotated))
def areConnected(a, b):
  edgesA = set([x for y in edges(a) for x in y])
  edgesB = set([x for y in edges(b) for x in y])
  return not edgesA.isdisjoint(edgesB)


def part1(input):
  shares = {k:set() for k in input.keys()}
  for ka, a in input.items():
    for kb, b in input.items():
      if ka == kb:
        continue
      if areConnected(a,b):
        shares[ka].add(kb)
  result = 1
  for x, y in shares.items():
    if len(y) == 2:
      result *= x
  return result, shares


def findCommonEdge(input, fixed, floating):
  edgesFixed = edges(input[fixed])
  

def buildImage(input):
  shares = part1(input)[1]
  board = [[0 for i in range(12)] for j in range(12)]
  for x in shares.keys():
    shares[x] = sorted(list(shares[x]))
  for x, y in shares.items():
    if len(y) == 2:
      board[0][0] = x
      break
  print(type(shares[board[0][0]]))
  
  # for x in board:
    # print(x)

def part2(input):
  # algoritam za tilanje
  # uzeti jedan cosak i na osnovu njega ici desno da se nadju svi tileovi do iduceg coska
      # kada se odredi tile, odma ga rotirati and or mirrorati da matchuje prethodnu ivicu
  # za svaki tile u redu traziti tileove ispod njega do kraja reda
      # kada se odredi tile, odma ga rotirati and or mirrorati da matchuje prethodnu ivicu
  buildImage(input)
  

  return "pog"

def day20(input, day):
  print("Day", day, "part1: ", part1(input)[0])
  print("Day", day, "part2: ", part2(input))

if __name__ == "__main__":
  from day20.input import input
  day = 20
  test = False
  # test = True
  file = "day%d/input.txt" % day
  if test:
    file = "test.txt"
  
  day20(input, day)