import time
import cProfile
def part(input, nth):
  seen = {x:i for i, x in enumerate(input)}
  temp = None
  next, last, num = 0, 0, len(input) 

  for i, x in enumerate(reversed(input[:-2])):
    if x == input[-1]:
      next=i+2
  for num in range(num, nth):
    temp = num-seen.get(next, num)
    seen[next] = num
    last, next = next, temp
  # print(len(seen))
  return last

def day15(input):
  print("Day", day, "part1: ", part(input, 2020))
  # cProfile.run("part(input, 30000000)")
  start = time.time()
  print("Day", day, "part2: ", part(input, 30000000))
  print(time.time()-start)

if __name__ == "__main__":
  day = 15
  input=[]
  file = "day%d/input.txt" % day
  for line in open(file, "r").readlines():
    input += [int(x) for x in line.split(",")]
  day15(input)