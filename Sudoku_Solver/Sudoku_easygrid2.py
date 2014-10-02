from SudokuSetup import *

easygrid = Grid()

easygrid.set_row(1, [5,0,8, 0,1,0, 7,0,3])
easygrid.set_row(2, [0,1,0, 0,0,0, 6,0,0])
easygrid.set_row(3, [3,0,0, 8,0,0, 2,4,0])
easygrid.set_row(4, [7,0,0, 3,2,8, 0,0,0])
easygrid.set_row(5, [6,3,0, 9,0,4, 0,7,2])
easygrid.set_row(6, [0,0,0, 1,6,7, 0,0,9])
easygrid.set_row(7, [0,8,6, 0,0,3, 0,0,7])
easygrid.set_row(8, [0,0,4, 0,0,0, 0,8,0])
easygrid.set_row(9, [2,0,3, 0,8,0, 4,0,5])
easygrid.print_me()

print "\nStart: "

for iter in range(0,10):
    print "\niteration: " + str(iter)
    easygrid.update_notpossibles()
    easygrid.print_me()

print "\nValidating solution..."
easygrid.validate()
