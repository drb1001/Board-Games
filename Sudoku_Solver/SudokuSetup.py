# thoughts:
# Identify the next (easy) move

class Cell(object):

    ## vars:
    # contents = int, 0 if unknown else (1-9) if content is known
    # possibles[] =  array of bool x10 , possible numbers ( 0 == False, 1-9 : true = could be, false = not)

    def __init__(self, contents=0):
        self.set_contents(contents)

    def set_contents(self, contents):
        self.contents = contents
        if self.contents == 0:
            self.possibles = [True] * 10
            self.possibles[0] = False
        else:
            self.possibles = [False] * 10
            self.possibles[contents] = True

    def is_known(self):
        if self.contents in range(1, 10):
            return True
        else:
            return False

    def set_notpossible(self, numbers_array):
        for number in numbers_array:
            self.possibles[number] = False
        if self.count_possibles() == 1:
            self.set_contents(self.get_possibles()[0])

    def get_possibles(self):
        return [ i for i in range(0,10) if self.possibles[i] ]

    def count_possibles(self):
        return len( self.get_possibles() )

    def print_cell(self):
        if self.is_known(): print self.contents
        if not self.is_known(): print self.get_possibles()


class Group(object):

    ## vars:
    # cells[] = array of 9 Cell objects
    # label = string, describing the type of group

    def __init__(self , cells_array, label):
        self.cells = cells_array
        self.label = label

    def contains_cell(self, cell):
        for grp_cell in self.cells:
                if cell is grp_cell:
                    return True
        return False

    def print_group(self):
        print "  printing group: %s" %self.label
        for cell in self.cells:
            cell.print_cell()

    def update_group_check(self):
        for test_n in range(1, 10):
            counter = 0
            skip = False
            for cell in self.cells:
                if cell.contents == test_n:
                    skip = True
                if cell.possibles[test_n]:
                    counter += 1
            if counter == 1 and skip == False:
                for cell in self.cells:
                    if cell.possibles[test_n]:
                        cell.set_contents(test_n)

    def update_group_doubles(self):
        for cell in self.cells:
            if len( cell.get_possibles() ) == 2:
                double_array = cell.get_possibles()
                for cell_2 in self.cells:
                    if ( cell_2 != cell ) and ( double_array == cell_2.get_possibles() ):
                        for cell_others in self.cells:
                            if cell_others != cell_2 and cell_others != cell:
                                cell_others.set_notpossible(double_array)

    def validate(self):
        check_array = []
        for cell in self.cells:
            check_array.append( cell.contents )
        check_array = sorted(check_array)
        if check_array != [1, 2, 3, 4, 5, 6, 7, 8, 9]:
            return ( False , "Invalid solution  - %s group is incorrect" %self.label )
        else:
            return ( True , "This group is valid" )


class Grid(object):

    ## vars:
    # cells[] = array of 81 Cell objects (as top right to bottom left)
    # groups[] = array of 27 group objects (9 rows, 9 columns, 9 boxes)

    def __init__(self, flat_array = [Cell(0)]*81):
        self.cells = []
        for x in flat_array:
            self.cells.append( Cell(x) )
        self.set_groups()

    @classmethod
    def from_string(cls, sudokustring):
        a = list(sudokustring)
        flat_array = [0 if x == "." else int(x) for x in a]
        return Grid(flat_array)

    @classmethod
    def from_square_array(cls, square_array):
        flat_array = [x for row in square_array for x in row]
        return Grid(flat_array)

    def set_groups(self):
        self.groups = []
        # rows
        for start_pos in range(0, 9):
            row_group = []
            for step in range(0, 9):
                row_group.append( self.cells[(start_pos * 9 + step)] )
            temp_group = Group(row_group , "row %s" %str(start_pos+1))
            self.groups.append( temp_group )
        # cols
        for start_pos in range(0, 9):
            col_group = []
            for step in range(0, 9):
                col_group.append( self.cells[(start_pos + step * 9)] )
                temp_group = Group(col_group , "col %s" %str(start_pos+1))
            self.groups.append( temp_group )
        # boxes
        for start_pos in [0,3,6,27,30,33,54,57,60]:
            box_group = []
            for step in [0,1,2,9,10,11,18,19,20]:
                box_group.append( self.cells[ start_pos + step ] )
                temp_group = Group(box_group , "box %s" %start_pos)
            self.groups.append( temp_group )

    def print_me(self):
        print " ----- ----- -----"
        for row_i in range(0, 9):
            row_string = "|"
            for col_j in range(0, 9):
                seperator = " "
                if col_j % 3 == 2:
                    seperator = "|"
                if self.cells[row_i * 9 + col_j].is_known():
                    row_string += str(self.cells[row_i * 9 + col_j].contents) + seperator
                else:
                    row_string += " " + seperator
            print row_string
            if row_i % 3 == 2:
                print " ----- ----- -----"

    def update_notpossibles(self):
        for cell in self.cells:
            if cell.is_known():
                continue
            for group in self.groups:
                if group.contains_cell(cell):
                    for grp_cell in group.cells:
                        if grp_cell.is_known():
                            cell.set_notpossible( [ grp_cell.contents ] )

    def update_groups_check(self):
        for group in self.groups:
            group.update_group_check()

    def update_groups_doubles(self):
        for group in self.groups:
            group.update_group_doubles()

    def is_grid_filled(self):
        for cell in self.cells:
            if not cell.is_known():
                return False
        return True

    def validate(self):
        # no empty cells
        if not self.is_grid_filled():
            return ( False , "invalid solution - incomplete grid")
        # check groups are valid (one of each 1-9)
        for group in self.groups:
            is_grp_valid, grp_valid_msg = group.validate()
            if not is_grp_valid:
                return (is_grp_valid , grp_valid_msg)
        else:
            return ( True , "This is a valid solution" )

    def solve(self, max_iters = 10, verbose = 0):
        print "\nStart: "
        self.print_me()
        for iter in range(0, max_iters):
            if verbose >= 1: print "\niteration: " + str(iter)
            self.update_notpossibles()
            if verbose >= 2: print "completed step 'update not possibles', iteration: " + str(iter)
            if verbose >= 2: self.print_me()
            self.update_groups_check()
            if verbose >= 2: print "completed step 'update groups check', iteration: " + str(iter)
            if verbose >= 2: self.print_me()
            self.update_groups_doubles()
            if verbose >= 2: print "complete step 'update groups doubles', iteration: " + str(iter)
            if verbose >= 1: self.print_me()
            if self.is_grid_filled():
                print "\nPuzzle Complete (on iteration %s):" %iter
                break
        self.print_me()
        print "Validating solution..."
        is_valid, valid_msg = self.validate()
        print valid_msg
