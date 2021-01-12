from day19.rules import rules
import re

rulesDone = {35: "b", 43: "a"}
rulesParse = rules

# Sample rules
# {
# ...
# 117: [[35,80],[43,10]],
# 17: [[43,112],[35,16]],
# 48: [[35,35]],
# 34: [[63,63]],
# 52: [[115,63]],
# 0: [[42,11]], 
# ...
# }

def allRulesDone(lst):
  for x in lst:
    if x not in rulesDone.keys():
      return False
  return True

while rulesParse:
  for x, rule in rulesParse.items():
    if len(rule) == 1:
      if allRulesDone(rule[0]):
        rulesDone[x] = "".join([rulesDone[y] for y in rule[0]])
      else:
        continue
    elif len(rule) == 2:
      if allRulesDone(rule[0]) and allRulesDone(rule[1]):
        rulesDone[x] = "(" + "".join([rulesDone[y] for y in rule[0]]) + "|" + "".join([rulesDone[y] for y in rule[1]]) + ")"
  for y in rulesDone.keys():
    rulesParse.pop(y, 0) 

day = 19
file = "day%d/input.txt" % day
input = [line.strip() for line in open(file, "r").readlines()]
counter = 0
for x in input:
  if re.fullmatch(rulesDone[0], x):
    counter+=1
print(counter)






