import unittest
from SudokuSetup import *


cell0 = Cell()
cell5 = Cell(5)
cell9 = Cell(0)
cell9.set_notpossible([1,2,3,7,8])

group1 = Group( [cell5, cell9, Cell(4), Cell(6), Cell(0), Cell(0), Cell(0), Cell(0), Cell(0) ] , "test group" )



class TestCellFunctions(unittest.TestCase):

    def test_contents(self):
        self.assertEqual( cell0.contents, 0 )
        self.assertEqual( cell5.contents, 5 )
        self.assertEqual( cell9.contents, 0 )

    def test_possibles(self):
        self.assertEqual( cell0.possibles, [False,True,True,True,True,True,True,True,True,True] )
        self.assertEqual( cell5.possibles, [False,False,False,False,False,True,False,False,False,False] )
        self.assertEqual( cell9.possibles, [False,False,False,False,True,True,True,False,False,True] )

    def test_is_known(self):
        self.assertEqual( cell0.is_known(), False )
        self.assertEqual( cell5.is_known(), True )
        self.assertEqual( cell9.is_known(), False )

    def test_get_possibles(self):
        self.assertEqual( cell0.get_possibles(), [1,2,3,4,5,6,7,8,9] )
        self.assertEqual( cell5.get_possibles(), [5] )
        self.assertEqual( cell9.get_possibles(), [4,5,6,9] )

    def test_count_possibles(self):
        self.assertEqual( cell0.count_possibles(), 9 )
        self.assertEqual( cell5.count_possibles(), 1 )
        self.assertEqual( cell9.count_possibles(), 4 )


class TestGroupFunctions(unittest.TestCase):

    def test_group_contains_cell(self):
        self.assertEqual( group1.contains_cell( cell0 ) , False )
        self.assertEqual( group1.contains_cell( cell5 ) , True )
        self.assertEqual( group1.contains_cell( cell9 ) , True )




if __name__ == '__main__':
    unittest.main()
