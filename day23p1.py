import time
class Node:
  def __init__(self, dataVal=None):
    self.dataVal = dataVal
    self.nextVal = None

def returnLinkedArray(input):
  test = [Node(i+1) for i in range(len(input))]
  # for i in range(len(input)):
  #   if i == len(input)-1:
  #     array[input[i]-1].nextVal = array[input[0]-1]
  #     break
  #   array[input[i]-1].nextVal = array[input[i+1]-1]
  # return array

  for i in range(len(test)):
    if i == len(test)-1:
      test[i].nextVal = test[0]
      break
    test[i].nextVal = test[i+1]
  return test

foo = time.time()
input = [3,9,4,6,1,8,5,2,7]
input += range(10, 1000001)
maxInput = 1000000
# input = [3,8,9,1,2,5,4,6,7]
# input+= range(10, 1000001)
bar = time.time()
array = returnLinkedArray(input)
print("could it be???", time.time()-bar)
for i in range(len(input)):
  if i == len(input)-1:
    array[input[i]-1].nextVal = array[input[0]-1]
    break
  array[input[i]-1].nextVal = array[input[i+1]-1]
print("could it be???", time.time()-bar)

num = input[0]
start = time.time()
for i in range(10000000):
  numNode = array[num-1]
  ######
  # odredi tri broja i zaobidji ih
  ######
  three = array[num-1].nextVal
  array[num-1].nextVal = three.nextVal.nextVal.nextVal

  ######
  # get destination
  ######
  dest = num-1
  if dest<1:
    dest = maxInput
  while dest == three.dataVal or dest == three.nextVal.dataVal or dest == three.nextVal.nextVal.dataVal:
    dest -= 1
    if dest < 1:
      dest = maxInput
  
  ######
  # umetni tri broja izmedju destination i iduceg
  ######
  three.nextVal.nextVal.nextVal = array[dest-1].nextVal
  array[dest-1].nextVal = three

  num = array[num-1].nextVal.dataVal
print("pog", time.time()-start)
temp = array[0].nextVal
print(temp.dataVal)
print(temp.dataVal * temp.nextVal.dataVal)

print(time.time()-foo)
# print("".join([str(x) for x in arr]))
# assert "".join([str(x) for x in arr]) == "92658374"