import time
from parse import parse
from itertools import product
import re

def part1(input):
  def decrypt(number, key):
    value, i = 1, 1
    while value != key:
      value *= number
      value %= 2020_1227 # 909_3927
      i+=1
    return i-1
  def encrypt(number, loopsize):
    value = 1
    for i in range(loopsize):
      value *= number
      value %= 2020_1227
    return value
  print(decrypt(7, 5764801))
  print(encrypt(17807724, 8))
  print(encrypt(11001876, decrypt(7, 9093927)) )
  # print(encrypt(decrypt(7, 9093927), decrypt(7, 11001876)))

  # print()
  
  return "not pog"

def part2(input):
  return "pog"

def day20(input, day):
  print("Day", day, "part1: ", part1(input))
  print("Day", day, "part2: ", part2(input))

if __name__ == "__main__":
  day = 25
  test = False
  # test = True
  file = "day%d/input.txt" % day
  if test:
    file = "test.txt"
  input = [9093927, 11001876]
  day20(input, day)