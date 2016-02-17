from dancing_links import *


# test_array =
# 	1	2	3	4	5	6	7
# A	1	0	0	1	0	0	1
# B	1	0	0	1	0	0	0
# C	0	0	0	1	1	0	1
# D	0	0	1	0	1	1	0
# E	0	1	1	0	0	1	1
# F	0	1	0	0	0	0	1


X1 = {1, 2, 3, 4, 5, 6, 7}
Y = {
    'A': [1, 4, 7],
    'B': [1, 4],
    'C': [4, 5, 7],
    'D': [3, 5, 6],
    'E': [2, 3, 6, 7],
    'F': [2, 7]}

X = {
    1: {'A', 'B'},
    2: {'E', 'F'},
    3: {'D', 'E'},
    4: {'A', 'B', 'C'},
    5: {'C', 'D'},
    6: {'D', 'E'},
    7: {'A', 'C', 'E', 'F'}}

# X = {j: set() for j in X}
#for i in Y:
#    for j in Y[i]:
#        X[j].add(i)


S = solve(X,Y)
print S
print X
print Y
