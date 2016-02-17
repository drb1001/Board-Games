# Credits for methods to Ali Assaf, see:  http://www.cs.mcgill.ca/~aassaf9/python/algorithm_x.html

def solve(X, Y, solution=[]):
    if not X:
        yield list(solution)
    else:
        c = min(X, key=lambda c: len(X[c]))
        for r in list(X[c]):
            solution.append(r)
            cols = select(X, Y, r)
            for s in solve(X, Y, solution):
                yield s
            deselect(X, Y, r, cols)
            solution.pop()
    print solution

def select(X, Y, r):
    cols = []
    for j in Y[r]:
        for i in X[j]:
            for k in Y[i]:
                if k != j:
                    X[k].remove(i)
        cols.append(X.pop(j))
    return cols

def deselect(X, Y, r, cols):
    for j in reversed(Y[r]):
        X[j] = cols.pop()
        for i in X[j]:
            for k in Y[i]:
                if k != j:
                    X[k].add(i)


# # Example of finding exact cover:
#
# 0010110
# 1001001
# 0110010
# 1001000
# 0100001
# 0001101
#
# # if empty, done
# # else, chose a column deterministic, c
# # choose a row r, such that a(r,c) == 1 (non-deterministically - how??)
# # include r in a partial solution
# # for each column j where a(r,j) == 1,
#   # delete column j from A
#   # for each row i where a(i,j) == 1
#     # delete row i from A
# # repeat
#
# # !! at each stage, choose the column with fewest 1s in the current matrix
#
# # ##############################################
# # #####  try 1 - start
#   0123456
# 0 0010110
# 1 1001001
# 2 0110010
# 3 1001000
# 4 0100001
# 5 0001101
#
# # choose column 6 ; choose row 1
#   0123456
# 0 0010110
# 1 1001001 *
# 2 0110010
# 3 1001000
# 4 0100001
# 5 0001101
#
# # remove col 0 (since [1,0] = 1); remove rows 1,3
# # remove col 3 (since [1,3] = 1); remove rows 1,3,5
# # remove col 6 (since [1,6] = 1); remove rows 1,4,5
#   1245
# 0 0111
# 2 1101
#
# # choose column 5 ; choose row 0
#   1245
# 0 0111 *
# 2 1101
#
# # remove col 2 (since [0,2] = 1); remove rows 0,2
# # remove col 4 (since [0,4] = 1); remove rows 0
# # remove col 5 (since [0,5] = 1); remove rows 0,5
# [] (empty array)
#
# selected rows = {0,1}
# cover = [1011111] (not complete)
#
#
# # ##############################################
# # #####  try 2 - start
#   0123456
# 0 0010110
# 1 1001001
# 2 0110010
# 3 1001000
# 4 0100001
# 5 0001101
#
# # choose column 0 ; choose row 3
#   0123456
# 0 0010110
# 1 1001001
# 2 0110010
# 3 1001000 *
# 4 0100001
# 5 0001101
#
# # remove col 0 (since [3,0] = 1); remove rows 1,3
# # remove col 3 (since [3,3] = 1); remove rows 1,3,5
#   12456
# 0 01110
# 2 11010
# 4 10001
#
# # choose column 4 ; choose row 0
#   12456
# 0 01110 *
# 2 11010
# 4 10001
#
# # remove col 2 (since [0,2] = 1); remove rows 0,2
# # remove col 4 (since [0,4] = 1); remove rows 0
# # remove col 5 (since [0,5] = 1); remove rows 0,2
#   16
# 4 11
#
# # choose column 1 ; choose row 4
#   16
# 4 11 *
#
# # remove col 1 (since [4,1] = 1); remove rows 4
# # remove col 6 (since [4,6] = 1); remove rows 4
#
# [] (empty array)
#
# selected rows = {0,3,4}
# cover = [1111111] (complete)
