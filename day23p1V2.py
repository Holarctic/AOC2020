import time

def returnLinkedArray(input):
  # test = [Node(i+1) for i in range(numOfItems)]
  numOfItems = len(input)
  test = [[i+1, None] for i in range(numOfItems)]
  for i in range(len(test)):
    if i == len(test)-1:
      test[input[i]-1][1] = test[input[0]-1]
      break
    test[input[i]-1][1] = test[input[i+1]-1]
  return test


# input = [3,9,4,6,1,8,5,2,7]
# input += range(10, 1000001)
maxInput = 9
input = [3,8,9,1,2,5,4,6,7]
# input+= range(10, 1000001)
array = returnLinkedArray(input)

num = input[0]
start = time.time()
for i in range(10000000):
  ######
  # odredi tri broja i zaobidji ih
  ######
  array[num-1][1] = array[num-1][1][1][1][1]

  ######
  # get destination
  ######
  dest = num-1
  if dest<1:
    dest = maxInput
  while dest == array[num-1][1][0] or dest == array[num-1][1][1][0] or dest == array[num-1][1][1][1][0]:
    dest -= 1
    if dest < 1:
      dest = maxInput
  
  ######
  # umetni tri broja izmedju destination i iduceg
  ######
  array[num-1][1][1][1][1] = array[dest-1][1]
  array[dest-1][1] = array[num-1][1]

  num = array[num-1][1][0]


print("pog", time.time()-start)
temp = array[0][1]
print(temp[0]) # 835237
print(temp[0] * temp[1][0]) # 565615814504



# time to beat 26s

# print("".join([str(x) for x in arr]))
# assert "".join([str(x) for x in arr]) == "92658374"