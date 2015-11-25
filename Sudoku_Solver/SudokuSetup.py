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
        output = []
        for i in range(0, 10):
            if self.possibles[i]:
                output.append(i)
        return output

    def count_possibles(self):
        return len(self.get_possibles())


class Grid(object):
    def __init__(self):
        self.cells = []
        for i in range(0, 9):
            temp_r = []
            for j in range(0, 9):
                c = Cell(0)
                temp_r.append(c)
            self.cells.append(temp_r)

    def set_row(self, row, num_array):
        for i in range(0, 9):
            self.cells[row - 1][i].set_contents(num_array[i])

    def print_me(self):
        print " ----- ----- -----"
        for row_i in range(0, 9):
            row_string = "|"
            for col_j in range(0, 9):
                seperator = " "
                if col_j % 3 == 2:
                    seperator = "|"
                if self.cells[row_i][col_j].is_known():
                    row_string += str(self.cells[row_i][col_j].contents) + seperator
                else:
                    row_string += " " + seperator
            print row_string
            if row_i % 3 == 2:
                print " ----- ----- -----"

    def update_notpossibles(self):
        for row_i in range(0, 9):
            for col_j in range(0, 9):
                if self.cells[row_i][col_j].is_known():
                    continue

                # check the row
                row_array = []
                for col_cell in range(0, 9):
                    if self.cells[row_i][col_cell].is_known() and col_cell != col_j:
                        row_array.append(self.cells[row_i][col_cell].contents)
                self.cells[row_i][col_j].set_notpossible(row_array)

                # check the col
                col_array = []
                for row_cell in range(0, 9):
                    if self.cells[row_cell][col_j].is_known() and row_cell != row_i:
                        col_array.append(self.cells[row_cell][col_j].contents)
                self.cells[row_i][col_j].set_notpossible(col_array)

                # check box
                box_array = []
                for row_cell in range(row_i//3 * 3, row_i//3 * 3 + 3):
                    for col_cell in range(col_j//3 * 3, col_j//3 * 3 + 3):
                        if self.cells[row_cell][col_cell].is_known() and row_cell != row_i and col_cell != col_j:
                            box_array.append(self.cells[row_cell][col_cell].contents)
                self.cells[row_i][col_j].set_notpossible(box_array)

    def update_rows_check(self):
        for row_i in range(0, 9):
            for test_n in range(1, 10):
                counter = 0
                for col_j in range(0, 9):
                    if self.cells[row_i][col_j].possibles[test_n]:
                        counter += 1
                if counter == 1:
                    for col_j in range(0, 9):
                        if self.cells[row_i][col_j].possibles[test_n]:
                            self.cells[row_i][col_j].set_contents(test_n)
                            break

    def update_cols_check(self):
        for col_j in range(0, 9):
            for test_n in range(1, 10):
                counter = 0
                for row_i in range(0, 9):
                    if self.cells[row_i][col_j].possibles[test_n]:
                        counter += 1
                if counter == 1:
                    for row_i in range(0, 9):
                        if self.cells[row_i][col_j].possibles[test_n]:
                            self.cells[row_i][col_j].set_contents(test_n)
                            break

    def update_box_check(self):
        for box_row in range(0, 9, 3):
            for box_col in range(0, 9, 3):
                for test_n in range(1, 10):
                    counter = 0
                    for row_cell in range(0, 3):
                        for col_cell in range(0, 3):
                            if self.cells[box_row + row_cell][box_col + col_cell].possibles[test_n]:
                                counter += 1
                    if counter == 1:
                        for row_cell in range(0, 3):
                            for col_cell in range(0, 3):
                                if self.cells[box_row + row_cell][box_col + col_cell].possibles[test_n]:
                                    self.cells[box_row + row_cell][box_col + col_cell].set_contents(test_n)

    def validate(self):
        # no empty cells
        for row_i in range(0, 9):
            for col_j in range(0, 9):
                if not self.cells[row_i][col_j].is_known():
                    print "invalid solution - incomplete grid"
                    return False
        # check rows are valid (one of each 1-9)
        for row_i in range(0, 9):
            check_array = []
            for col_j in range(0, 9):
                check_array.append(self.cells[row_i][col_j].contents)
            check_array = sorted(check_array)
            if check_array != [1, 2, 3, 4, 5, 6, 7, 8, 9]:
                print "invalid solution  - row is incorrect: ", row_i
                return False
        # check columns are valid (one of each 1-9)
        for col_j in range(0, 9):
            check_array = []
            for row_i in range(0, 9):
                check_array.append(self.cells[row_i][col_j].contents)
            check_array = sorted(check_array)
            if check_array != [1, 2, 3, 4, 5, 6, 7, 8, 9]:
                print "invalid solution  - row is incorrect: ", col_j
                return False
        # check boxes are valid (one of each 1-9) TBD

        else:
            print "This is a valid solution"
            return True