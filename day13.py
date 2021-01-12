from downloadInput import start
from parse import parse
import time
day = 13
input=[]
file = "day%d/input.txt" % day
# file = "test.txt"
lines = open(file, "r").readlines()
t = int(lines[0])
input = [int(x) if x!= "x" else "x" for x in lines[1].split(",")]
input = [t, input]

def part1(input):
  minTime = input[1][0]
  for x in input[1]:
    if x != "x":
      if (x-input[0]%x) < (minTime - input[0]%minTime):
        minTime = x
  return minTime * (minTime - input[0]%minTime)



def part2(input):
  def extended_euclidean(a, b): 
    if a == 0: 
      return (b, 0, 1) 
    else: 
      g, y, x = extended_euclidean(b % a, a) 
      return (g, x - (b // a) * y, y) 

  # modular inverse driver function 
  def modinv(a, m): 
    g, x, y = extended_euclidean(a, m) 
    return x % m 

  # function implementing Chinese remainder theorem 
  # list m contains all the modulii 
  # list x contains the remainders of the equations 
  def crt(m, x): 

    # We run this loop while the list of 
    # remainders has length greater than 1 
    while True: 
      
      # temp1 will contain the new value 
      # of A. which is calculated according 
      # to the equation m1' * m1 * x0 + m0' 
      # * m0 * x1 
      temp1 = modinv(m[1],m[0]) * x[0] * m[1] + modinv(m[0],m[1]) * x[1] * m[0] 

      # temp2 contains the value of the modulus 
      # in the new equation, which will be the 
      # product of the modulii of the two 
      # equations that we are combining 
      temp2 = m[0] * m[1] 

      # we then remove the first two elements 
      # from the list of remainders, and replace 
      # it with the remainder value, which will 
      # be temp1 % temp2 
      x.remove(x[0]) 
      x.remove(x[0]) 
      x = [temp1 % temp2] + x 

      # we then remove the first two values from 
      # the list of modulii as we no longer require 
      # them and simply replace them with the new 
      # modulii that we calculated 
      m.remove(m[0]) 
      m.remove(m[0]) 
      m = [temp2] + m 

      # once the list has only one element left, 
      # we can break as it will only contain 
      # the value of our final remainder 
      if len(x) == 1: 
        break

    # returns the remainder of the final equation 
    return x[0] 

  input = [(x, i) for i,x in enumerate(input[1]) if x!="x"] 
  return crt([x[0] for x in input], [x-i for x,i in input])/input[0][0]


def day13(input):
  print("Day 13 part1: ", part1(input))
  print("Day 13 part2: ", part2(input))

day13(input)