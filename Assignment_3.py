import numpy as np

class Entry:
    '''
    info about a_{i j} of a matrix\n
    change this when you change a value in an entry in any way\n
    essentially a set of variables describing an object
    '''
    def __init__(self,
                 value,
                 row : int,
                 col : int
                 ):
        self.value = value
        self.row = row
        self.col = col
        self.type = type(value)
        self.name = [self.row, self.col]

class Matrix:
    '''
    useful for matrix stuff
    '''
    def __init__(
            self,
            name : str,
            entries : list[Entry],
            dimensions : tuple
            ):
        self.name = name

        self.dimensions = (None, None)
        self.determinant = None
        self.entries = entries
        self.show_dp = 2
    
    def __str__(self):
        s = f"{self.name} is a {self.num_rows}x{self.num_cols} matrix"
        if self.entries is not None
            s += '\n\n'
            for row in range(self.num_rows):
                s += '\t'
                for col in range(self.num_cols):
                    s += str(round(self.get_entry_value(row,col),self.show_dp))
                    s += '   '
                s += '\n'
        return s

    @property
    def num_rows(self):
        return self.dimensions[0]

    @property
    def num_cols(self):
        return self.dimensions[1]

    @property
    def is_square(self):
        return (self.num_rows == self.num_cols) and (self.num_cols is not None)

    def update_dimensions(self, num_rows : int, num_cols : int):
        self.dimensions = (num_rows,num_cols)

    def update_all_values(self, entries : tuple)
        '''
        takes tuple of new set of entries for entire 
        '''
        if len(entries) != (self.num_cols * self.num_rows)
            print(f"ERROR: number of entries ({len(entries)}) does not match {self.num_rows}x{self.num_cols} matrix")
            return

        self.entries = 

    def get_entry_index(self, row : int, col : int) -> int:
        '''
        returns the 0-indexed position of the entry in `row`,`col` for matrix stored in list
        '''
        return (self.num_cols * row) + col

    def get_entry_value(self, row : int, col : int) -> float:
        '''
        returns the value of the entry in `row`,`col`
        '''
        return self.entries[self.get_entry_index(row,col

    def update_entry_value(self, index, value):
        '''
        updates the vale of element at `index`\n
        use `self.get_entry_index(row, col)` to get index
        '''
        self.entries[index] = 

    def get_row_values(self, row : int) -> tuple:
        '''
        returns a tuple of entries in `row
        '''
        return [
            self.get_entry_value(row, i)
            for i in range(self.num_cols)
            ]

    def get_col_values(self, col : int) -> tuple:
        '''
        returns a tuple of entries in `col
        '''
        return ([
            self.get_entry_value(i, col)
            for i in range(self.num_rows)
            ])

    def update_row_values(self, row, vals):
    
        row_start_index = self.get_entry_index(row,0)
        for i,val in enumerate(vals):
            self.update_entry_value(
                row_start_index + i,
                val
                )

    def append_to_rows(self, new_vals : tuple):
        '''
        
        '''
        if len(new_vals) != self.num_rows:
            print("ERROR: Number of rows in `new_vals` is not equal to number of rows in matrix")
            print(f"(New) {len(new_vals)} != {self.num_rows} ({self.name})")
        self.update_num_cols(self.num_cols + 1)
        for row in range(self.num_rows):
            self.update_row_values(row, new_vals[row])

    def append_col(self, col : tuple):
        if len(col) != self.num_rows:
            print("ERROR: Number of rows in col doesn't match matrix rows")
            return
        self.update_dimensions(self.num_rows, self.num_cols + 1)
        for row in range(self.num_rows):
            self.update_row_values()


A_VALS = [
    -1.5,  2.3,  0.3,  0.3,  0.5,
    -1.4,  1.5,  2.1, -0.2, -1.6,
    -0.1, -0.3,  2.3,  0.9,  0.4,
     0.6,  0.8,  1.7, -2.4,  1.7,
    -0.2,  0.4, -0.2,  1.1, -0.9
]

B_VALS = [
     -7.7,
    -13.9,
    -34.4,
    -43.5,
      12
]

entriesA = [Entry(val, row, col) for val in A_VALS for row in range]

a = Matrix('A', 5, 5, A)
print(a)
a.append_col(B)
print(a)