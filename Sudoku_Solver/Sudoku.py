
def get_possibles(grid, row, col):
    output = []
    for i in range(0,9):
        if grid[row][col][i]:
            output.append(i+1)
    return output

def print_grid(grid):
    for row_i in range(0,9):
        row_string = "[ "
        for col_j in range(0,9):
            if len(get_possibles(grid, row_i, col_j)) == 1:
                row_string = row_string + str(get_possibles(grid, row_i, col_j)[0]) + " "
            else:
                row_string = row_string + ". "

        print row_string + "]"


cell = [True] * 9
grid = [[cell] * 9] * 9

print_grid(grid)
print grid[1][2]
print get_possibles(grid,1,2)
print "--"

grid[1][2] = [True, False, False, False, False, False, False, False, False]
print_grid(grid)
print grid[1][2]
print get_possibles(grid,1,2)
print "-- --"

#
# for row_i in range(0,9):
#     for col_j in range(0,9):
#
#         print row_i, col_j, get_possibles(grid, row_i, col_j)
#
#         if len(get_possibles(grid, row_i, col_j)) == 1:
#             continue
#
#         # check the row
#         row_array = []
#         for row_cell in range(0,9):
#             if len(get_possibles(grid,row_i,row_cell)) == 1:
#                 row_array.append(get_possibles(grid,row_i,row_cell)[0])
#         for entry in row_array:
#                 grid[row_i][col_j][entry-1] = False
#         print row_array
#
#
#         # check the col
#         col_array = []
#         for col_cell in range(0,9):
#             if len(get_possibles(grid,col_cell,col_j)) == 1:
#                 col_array.append(get_possibles(grid,col_cell,col_j)[0])
#         for entry in col_array:
#                 grid[row_i][col_j][entry-1] = False
#         print col_array
#
#         # get distinct knowns distinct for box
#         get_possibles(grid, row_i, col_j)
#         print "-----"
#
# print "-- --"


print_grid(grid)
print grid[1][2]
print grid[1][3]