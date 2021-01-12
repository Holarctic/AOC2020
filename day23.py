import time
from parse import parse
from itertools import product
import re

start = time.time()

def timer(foobar):
  global start
  if not foobar%10000:
    print(foobar/10000, time.time() - start)
    start = time.time()

def part1(input):
  def result(input):
    pos = input.index(1)
    result = [str(input[x%len(input)]) for x in range(pos+1, pos+9)]
    return "".join(result)
  def pickThree(input, num):
    pos = input.index(num)
    three = [input[x%len(input)] for x in range(pos+1, pos+4)]
    input = [x for x in input if x not in three]
    return input, three
  def returnThree(input, num, three):
    pos = input.index(num)+1
    input[pos:pos] = three
    return input
  def findDest(input, num):
    num-=1
    while num not in input:
      num -= 1
      if num < 1:
        num=9
    return num
  def test(input):
    print("".join([str(x) for x in input]))
  num = input[0]
  for foobar in range(100):
    input, three = pickThree(input, num)
    # test(input)
    # test(three)
    dest = findDest(input, num)
    input = returnThree(input, dest, three)
    num = input[(input.index(num)+1)%len(input)]

  return result(input)

def part2(input):
  def pickThree(input, num):
    pos = input.index(num)
    three = [input.pop(x%len(input)) for x in range(pos+4, pos+1, -1)]
    return input, three
  def returnThree(input, num, three):
    pos = input.index(num)+1
    input[pos:pos] = three
    return input
  def findDest(input, num, three):
    temp = num
    num-=1
    if num < 1:
      num = 9
    while num in three:
      num -= 1
      if num < 1:
        num=9
    # if num<1:
      # num=9
    if num == 0:
      print(three, input, temp)    
    return num


  # input += range(10, 10**6+1)
  numIdx = 0
  num = input[0]
  # print(input)
  # for foobar in range(10000000):
  for foobar in range(100):
    # timer(foobar)
    if num == 0:
      print(three)
      exit()
    input, three = pickThree(input, num)
    # print(input, three)
    dest = findDest(input, num, three)
    input = returnThree(input, dest, three)
    
    num = input[(input.index(num)+1)%len(input)]
  one = input.index(1)
  return input
  return input[(one+1)%len(input)] * input[(one+2)%len(input)]

def day20(input, day):
  print("Day", day, "part1: ", part1(input))
  print("Day", day, "part2: ", part2(input))

if __name__ == "__main__":
  day = 23
  test = False
  test = True
  file = "day%d/input.txt" % day
  if test:
    file = "test.txt"
  input = [int(x) for x in open(file, "r").readline()]
  # input = [1,2,3,4,5,6,7,8,9]
  day20(input, day)