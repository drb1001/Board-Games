from SudokuSetup import *

easygrid = Grid()

easygrid.set_row(1, [9,4,0, 0,0,0, 0,0,0])
easygrid.set_row(2, [0,2,5, 0,8,4, 1,0,9])
easygrid.set_row(3, [6,3,1, 7,0,0, 0,0,0])
easygrid.set_row(4, [4,5,0, 9,0,0, 0,0,3])
easygrid.set_row(5, [0,0,0, 8,5,1, 0,0,0])
easygrid.set_row(6, [8,0,0, 0,0,6, 0,5,7])
easygrid.set_row(7, [0,0,0, 0,0,7, 3,6,1])
easygrid.set_row(8, [1,0,9, 3,6,0, 2,8,0])
easygrid.set_row(9, [0,0,0, 0,0,0, 0,9,5])
easygrid.print_me()

print "\nStart: "

for iter in range(0,10):
    print "\niteration: " + str(iter)
    easygrid.update_notpossibles()
    easygrid.print_me()

print "\nValidating solution..."
easygrid.validate()