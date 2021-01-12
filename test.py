test = {1:["123","456","789"]}
def rotate(piece):
  return ["".join(x) for x in list(map(list, zip(*piece)))]
def t(input):
  input[1] = rotate(input[1])
  # for x in input[1]:
  #   print(x)
t(test)
for x in test[1]:
  print(x)
def rotate(piece):
  return ["".join(x) for x in list(map(list, zip(*piece)))]
def edges(piece):
  temp = rotate(piece)
  edge = [piece[0], piece[-1], temp[0], temp[-1]]
  rotated = [x[::-1] for x in edge]
  return list(zip(edge, rotated))
# print(edges(test[1]))