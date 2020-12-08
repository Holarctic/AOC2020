input=[]
for line in open("day8/input.txt", "r").readlines():
  cmd, val = tuple(line.split(" "))
  input.append([cmd, int(val)])

def program(input): 
  acc =0
  instruction = 0
  executed = []
  while instruction not in executed and instruction < len(input):
    executed.append(instruction)

    # instructions = ["nop", "acc", "jmp", ]
    if input[instruction][0] == "nop":
      instruction = instruction+1
    elif input[instruction][0] == "acc":
      acc = acc + input[instruction][1]
      instruction = instruction+1
    elif input[instruction][0] == "jmp":
      instruction = instruction + input[instruction][1]
    else:
      print("Unhandled instruction, you suck")

  return acc, not instruction < len(input), executed
  
acc, done, executed = program(input)
print("not pog", acc)

# part2
executed = [x for x in executed if (input[x][0]!="acc" or input[x][0]=="jmp")]

for i in executed:
  if done:
    print("pog", acc)
    break
  else:
    instruction, input[i][0] = input[i][0], (input[i][0] == "nop" and "jmp" or "nop")
    acc, done, ex = program(input)
    input[i][0] = instruction
