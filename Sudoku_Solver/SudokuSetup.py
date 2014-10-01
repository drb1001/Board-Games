class Cell(object):
    def __init__(self, contents=0):
        self.contents = contents
        if self.contents == 0:
            self.possibles = [True] * 10
            self.possibles[0] = False
        else:
            self.possibles = [False] * 10
            self.possibles[contents] = True

    def set_contents(self, contents):
        self.contents = contents

    def is_known(self):
        if self.contents in range(1, 10):
            return True
        else:
            return False

    def set_notpossible(self, numbers_array):
        for number in numbers_array:
            self.possibles[number] = False
            if self.count_possibles() == 1:
                self.contents = self.get_possibles()[0]

    def get_possibles(self):
        output = []
        for i in range(0,10):
            if self.possibles[i]:
                output.append(i)
        return output

    def count_possibles(self):
        return len(self.get_possibles())


class Grid(object):
    def __init__(self):
        self.cells =[]
        for i in range(0, 9):
            temp_r = []
            for j in range(0, 9):
                c = Cell(0)
                temp_r.append(c)
            self.cells.append(temp_r)

    def set_row(self, row, num_array):
        for i in range(0,9):
            self.cells[row - 1][i].set_contents(num_array[i])

    def get_possibles(self, row, col):
        output = []
        for i in range(0,9):
            if self.cells[row][col].is_known:
                output.append(i+1)
        return output

    def print_me(self):
        print " ----- ----- -----"
        for row_i in range(0,9):
            row_string = "|"
            for col_j in range(0,9):
                seperator = " "
                if (col_j  % 3 == 2):
                    seperator = "|"
                if self.cells[row_i][col_j].is_known():
                    row_string += str(self.cells[row_i][col_j].contents) + seperator
                else:
                    row_string += " " + seperator
            print row_string
            if row_i % 3 == 2:
                print " ----- ----- -----"

    def update_notpossibles(self):
        for row_i in range(0,9):
            for col_j in range(0,9):
                if self.cells[row_i][col_j].is_known():
                    continue

                # check the row
                row_array = []
                for row_cell in range(0,9):
                    if self.cells[row_i][row_cell].is_known():
                        row_array.append(self.cells[row_i][row_cell].contents)
                self.cells[row_i][col_j].set_notpossible(row_array)

                # check the col
                col_array = []
                for col_cell in range(0,9):
                    if self.cells[col_cell][col_j].is_known():
                        col_array.append(self.cells[col_cell][col_j].contents)
                self.cells[row_i][col_j].set_notpossible(col_array)

                # check box
                box_array = []
                for row_cell in range(row_i//3 * 3, row_i//3 * 3 + 3):
                    for col_cell in range(col_j//3 * 3 , col_j//3 * 3 + 3):
                        if self.cells[row_cell][col_cell].is_known():
                            box_array.append(self.cells[row_cell][col_cell].contents)
                self.cells[row_i][col_j].set_notpossible(box_array)

    def validate(self):
        for row_i in range(0,9):
            for col_j in range(0,9):
                if not self.cells[row_i][col_j].is_known():
                    print "not solved - incomplete grid"
                    return False
        # need to add a check if all rows, columns and boxes are 1-9
        else:
            print "This is a valid solution"
            return True