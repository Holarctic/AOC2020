from parse import parse
day = 9
input=[]
file = "day%d/input.txt" % day
for line in open(file, "r").readlines():
  input.append(parse("{:d}", line)[0])

def isSum(arr, numb):
  for i in range(len(arr)):
    for j in range(i, len(arr)):
      if(arr[i] + arr[j] == numb):
        return True
  return False

Result = 0
for  i in range(len(input)):
  if i < 25:
    continue
  if not isSum(input[i-25:i], input[i]):
    print(input[i])
    Result = input[i]
    break

for i in range(len(input)):
  sum = 0
  for j in range(i, len(input)):
    sum += input[j]
    if sum == Result:
      temp = sorted(input[i:j+1])
      print(temp[0], temp[-1], temp[0] + temp[-1])
