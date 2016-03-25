import random
import itertools

large_numbers = [25,50,75,100]
small_numbers = range(1,11)*2

print selection
# choose whether to pick random numbers, or to type in numbers, or a selection.
large_count = raw_input("How many large numbers? (0-4): ")
if large_count == "n":
    target = int( raw_input("Enter your target: ") )
    selection = raw_input("Enter your numbers (space seperated): ")
    selection = [int(x) for x in selection.split()]
else:
    large_count = int(large_count)
    selection_large = random.sample( large_numbers, large_count )
    selection_small = random.sample( small_numbers, (6-large_count) )
    selection = selection_large + selection_small
    target = random.choice(range(101,1000))

target = random.choice(range(101,1000))
print target

# choose whether to pick random numbers, or to type in numbers.
# wait for input (do an actual countdown)

solutions = []
# solver: operations are: + - * /

#[50, 8, 4, 5, 1, 7]
#894

# generate permutations:
selection = selection + [0]
permutations = itertools.permutations(selection)
perms = list(permutations)
print len(perms)

perms_new = []

for p in perms:
    pos = p.index(0)
    temp = p[0:pos]
    print p, "\t", temp
    perms_new.append(temp)

print perms_new
print len(perms_new)
print len(set(perms_new))

# x + x + x + x + x + x + 0
# 7^6*4^6


# check each number
for x1 in selection:
    if x1 == target: solutions.append(str(x))

# for x1,x2 in selection:
#     if x1 + x2 == target: solutions.append(str(x1)+"+"+str(x2))
#     if x1 * x2 == target: solutions.append(str(x1)+"*"+str(x2))
#     if x1 - x2 == target: solutions.append(str(x1)+"-"+str(x2))
#     if x2 - x1 == target: solutions.append(str(x2)+"-"+str(x1))
#     if x1 / x2 == target: solutions.append(str(x1)+"/"+str(x2))
#     if x2 / x1 == target: solutions.append(str(x2)+"/"+str(x1))
#
# for x1,x2,x3 in selection:
#     if x1 + x2 + x3 == target: solutions.append(str(x1)+"+"+str(x2)+"+"+str(x3))
#     if x1 * x2 * x3 == target: solutions.append(str(x1)+"*"+str(x2)+"+"+str(x3))
#     if x1 - x2 == target: solutions.append(str(x1)+"-"+str(x2))
#     if x2 - x1 == target: solutions.append(str(x2)+"-"+str(x1))
#     if x1 / x2 == target: solutions.append(str(x1)+"/"+str(x2))
#     if x2 / x1 == target: solutions.append(str(x2)+"/"+str(x1))

# x + x + x
# x + x + x + x + x + x


# print len(solutions)
# print solutions
