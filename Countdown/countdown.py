import random
import itertools

large_numbers = [25,50,75,100]
small_numbers = range(1,11)*2

selection_large = random.sample( set(large_numbers), 1 )
selection_small = random.sample( set(small_numbers), 5 )
selection = selection_large + selection_small
print selection

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
