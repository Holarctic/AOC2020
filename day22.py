import time
from parse import parse
from itertools import product

def calculateResult(player):
  return sum([(i+1)*x for i, x in enumerate(list(reversed(player)))])


def part1(input):
  player1 = input[0].copy()
  player2 = input[1].copy()

  while player1 and player2:
    c1, c2 = player1.pop(0), player2.pop(0)
    if c1 > c2:
      player1 += [c1, c2]
    else:
      player2 += [c2, c1]

  if player1:
    return calculateResult(player1)
  else:
    return calculateResult(player2)


def recursiveCombat(player1, player2):
  player1Played = []
  player2Played = []
  while player1 and player2:
    if player1 in player1Played or player2 in player2Played:
      return True
    player1Played.append(player1.copy())
    player2Played.append(player2.copy())
    c1 = player1.pop(0)
    c2 = player2.pop(0)
    if c1 <= len(player1) and c2 <= len(player2):
      if recursiveCombat(player1[:c1], player2[:c2]):
        player1 += [c1, c2]
      else:
        player2 += [c2, c1]
    else:
      if c1 > c2:
        player1 += [c1, c2]
      else:
        player2 += [c2, c1]
  return not player2


def part2(input):
  player1 = input[0].copy()
  player2 = input[1].copy()
  player1Played = []
  player2Played = []
  
  while player1 and player2:
    if player1 in player1Played or player2 in player2Played:
      return calculateResult(player1)
    player1Played.append(player1.copy())
    player2Played.append(player2.copy())

    c1 = player1.pop(0)
    c2 = player2.pop(0)
    if c1 <= len(player1) and c2 <= len(player2):
      if recursiveCombat(player1[:c1], player2[:c2]):
        player1 += [c1, c2]
      else:
        player2 += [c2, c1]
    else:
      if c1 > c2:
        player1 += [c1, c2]
      else:
        player2 += [c2, c1]

  if player1:
    return calculateResult(player1)
  else:
    return calculateResult(player2)

def day19(input, day):
  print("Day", day, "part1: ", part1(input))
  print("Day", day, "part2: ", part2(input))

if __name__ == "__main__":
  day = 22
  test = False
  # test = True
  input = [[28, 13, 25, 16, 38, 3, 14, 6, 29, 2, 47, 20, 35, 43, 30, 39, 21, 42, 50, 48, 23, 11, 34, 24, 41],
  [27, 37, 9, 10, 17, 31, 19, 33, 40, 12, 32, 1, 18, 36, 49, 46, 26, 4, 45, 8, 15, 5, 44, 22, 7]]
  if test: 
    input = [[9, 2, 6, 3, 1], [5, 8, 4, 7, 10]]
  day19(input, day)