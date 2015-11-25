from SudokuSetup import *
from puzzles import *
# import testing_lib as tst

testgrid = Grid.from_string(easygrid_1_str)
print "\n\nTest: 'easygrid_1_str'"
testgrid.solve(max_iters = 10, verbose = 0)

testgrid = Grid.from_square_array(easygrid_1)
print "\n\nTest: 'easygrid_1'"
testgrid.solve(max_iters = 10, verbose = 0)

testgrid = Grid.from_square_array(easygrid_2)
print "\n\nTest: 'easygrid_2'"
testgrid.solve(max_iters = 10, verbose = 0)

testgrid = Grid.from_square_array(mediumgrid_1)
print "\n\nTest: 'mediumgrid_1'"
testgrid.solve(max_iters = 10, verbose = 0)

testgrid = Grid.from_square_array(evilgrid_1)
print "\n\nTest: 'evilgrid_1'"
testgrid.solve(max_iters = 20, verbose = 0)

testgrid = Grid.from_string(evilgrid_2_str)
print "\n\nTest: 'evilgrid_2_str'"
testgrid.solve(max_iters = 20, verbose = 0)

testgrid = Grid.from_string(evilgrid_3_str)
print "\n\nTest: 'evilgrid_3_str'"
testgrid.solve(max_iters = 20, verbose = 0)

testgrid = Grid.from_string(evilgrid_4_str)
print "\n\nTest: 'evilgrid_4_str'"
testgrid.solve(max_iters = 20, verbose = 0)
