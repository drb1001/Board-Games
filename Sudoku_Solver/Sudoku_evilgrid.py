from SudokuSetup import *

evilgrid = Grid()

evilgrid.set_row(1, [0,7,9, 0,0,0, 5,6,0])
evilgrid.set_row(2, [0,0,0, 8,6,0, 0,3,9])
evilgrid.set_row(3, [0,0,0, 5,0,0, 0,0,7])
evilgrid.set_row(4, [0,0,0, 0,0,3, 4,8,0])
evilgrid.set_row(5, [0,0,0, 0,0,0, 0,0,0])
evilgrid.set_row(6, [0,6,2, 4,0,0, 0,0,0])
evilgrid.set_row(7, [4,0,0, 0,0,6, 0,0,0])
evilgrid.set_row(8, [9,1,0, 0,7,8, 0,0,0])
evilgrid.set_row(9, [0,2,6, 0,0,0, 7,5,0])
evilgrid.print_me()

print "\nStart: "

for grid_pass in range(1, 100):
    print "\n* iteration: " + str(grid_pass)

    evilgrid.update_notpossibles()
    evilgrid.print_me()
    print "completed: update not possibles, iteration: " + str(grid_pass)

    evilgrid.update_rows_check()
    evilgrid.print_me()
    print "completed: update rows check, iteration: " + str(grid_pass)

    evilgrid.update_cols_check()
    evilgrid.print_me()
    print "completed: update columns check, iteration: " + str(grid_pass)

    evilgrid.update_box_check()
    evilgrid.print_me()
    print "complete: update box check, iteration: " + str(grid_pass)


print "\nValidating solution..."
evilgrid.validate()