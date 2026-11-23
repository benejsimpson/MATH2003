import numpy as np

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

class Matrix:
    '''
    stores a np.array of entries and gives operations to perform on them as a matrix.
    '''

    def __init__(
            self,
            name : str,
            values,
            is_augmented : bool = False,
            ):
        self.name = name
        self.data = np.array(values, dtype=float)
        self.is_augmented = is_augmented
        if self.data.ndim != 2:
            raise ValueError(f"Matrix must be 2 dimensions\n\tDim({self.name}) = {self.data.ndim}")

        self.show_dp = 2

#   ===========================
#   Properties
#   ===========================

    @property
    def dimensions(self):
        return self.data.shape

    @property
    def num_rows(self) -> int:
        return self.dimensions[0]

    @property
    def row_indices(self) -> tuple:
        return range(self.num_rows)

    @property
    def col_indices(self) -> tuple:
        return range(self.num_cols)

    @property
    def num_cols(self) -> int:
        return self.dimensions[1]

    @property
    def is_square(self) -> bool:
        '''
        returns true if matrix is square
        '''
        return (self.num_rows == self.num_cols)

#   ===========================
#   Construction & Validation
#   ===========================

    def update_entry_value(
            self,
            row : int,
            col : int,
            value
            ):
        '''
        updates the vale of element at `row`,`col`
        '''
        self.data[row,col] = value

#   ===========================
#   Representation
#   ===========================

    def __str__(self):
        s = f"{self.name} is a"
        if self.is_augmented:
            s += "n augmented"
        s += f" {self.num_rows}x{self.num_cols} matrix"
        s += '\n\n'
        for row in self.data:
            s += f"\t{[round(i,self.show_dp) for i in row]}\n"
        return s

#   ===========================
#   Indexing & Value Access
#   ===========================

    def get_entry_value_from_row_col(self, row : int, col : int) -> float:
        '''
        returns the value of the entry in `row`,`col`
        '''
        return self.data[row,col]

    def get_row_values(
        self,
        row : int
        ) -> list:
        '''
        returns values of `row` (row is 0-indexed)\n\n
        [   \n\t
            [ 00, 01, 02, ..., 0n],     <- row = 0\n\t
            [ 10, 11, 12, ..., 1n],     <- row = 1\n\t
                      .
                      .
                      .
            [ m0, m1, m2, ..., mn]      <- row = m\n
                                    ]
        '''
        return self.data[row,:]

    def get_col_values(
            self,
            col : int
        ) -> tuple:
        '''
        returns a tuple of entries in `col`
        '''
        return self.data[:,col]

#   ===========================
#   Elementary Row Operations
#   ===========================

    def scalar_multiply_row(
            self,
            row : int,
            scalar : float
    ):
        '''
        docstring
        '''
        self.data[row] *= scalar
        print(f"R{row} x {scalar}")

    def swap_rows(
            self,
            row1 : int,
            row2 : int
            ):
        '''
        swaps two rows
        '''
        self.data[[row1,row2]] = self.data[[row2,row1]]
        print(f"R{row1} <-> R{row2}")

    def subtract_multiple_of_row(
            self,
            row_being_subtracted_from : int,
            row_to_subtract : int,
            multiple = 1
    ):
        '''
        docstring
        '''
        self.data[row_being_subtracted_from] -= multiple * self.data[row_to_subtract]
        print(f"R{row_being_subtracted_from} - {round(multiple,self.show_dp)}x R{row_to_subtract}")

    def augment(
            self,
            new_vals : Matrix
        ):
        '''
        docstring
        '''
        if len(new_vals.dimensions) != 2 or new_vals.dimensions[0] != self.num_rows:
            raise ValueError(
                f"ERROR: Number of rows in `new_vals` is not equal to number of rows in matrix\n\t(New) {len(new_vals)} != {self.num_rows} ({self.name})"
                )

        self.data = np.column_stack((self.data,new_vals.data))
        self.is_augmented = True
    
    def get_augmented_col_values(self):
        '''
        ds
        '''
        if self.is_augmented:
            return self.get_col_values(self.num_cols-1)
        return None

class GaussianElimination(Matrix):
    '''
    algorithms for Guassian Elimination operations on a Matrix.\n
    Used to solve Ax=b, where:
    \n\t- `A` is a square nxn matrix representing a system of equations
    \n\t- `b` is a 1xn vector
    \nThe algorithm can be used to find a 1xn vector `x` representing the solutions to n variables in A
    '''
    def __init__(
            self,
            matrix
            ):
        # the matrix being operated on
        self.matrix = matrix
        # true if matrix is augmented matrix
        self.augmented = self.matrix.is_augmented
        # vector of solutions to variables
        self.x_vec = (None for _ in self.matrix.row_indices)

#   ===========================
#   Pivot Selection
#   ===========================

    def is_pivot_col(self, col : int) -> bool:
        '''
        returns true if column is all zeros and one 1
        '''
        col_vals = self.matrix.get_col_values(col)
        return (set(col_vals) == {0,1} and sum(col_vals) == 1)

    def get_index_of_first_nonzero_in_row(self, row : int) -> int:
        '''
        returns the index of first non-zero entry in R[`row`]
        '''
        for row_val,row_ind in enumerate(self.matrix.get_row_values(row)):
            if row_val != 0:
                return row_ind
        raise ValueError (f"R{row} is all zeros:\n\tR{row} = {self.matrix.get_row_values(row)}")
    
    def get_pivot_index_from_list(self, vals):
        '''
        takes a list/tuple/np.array of values and returns the 
        '''
        if type(vals) not in (tuple,list):
            vals = tuple(vals)

        return vals.index(1)

    def get_all_rows_with_pivots(self) -> tuple:
        '''
        returns a tuple of bools: res[i] = true if col[i] is a pivot column - has all zeros except for a leading 1\n
        ignores augmented column
        '''
        if self.matrix.is_augmented:
            cols = self.matrix.col_indices[:-1]
        else:
            cols = self.matrix.col_indices

        return [self.is_pivot_col(col) for col in cols]

    def make_pivot_in_col(self, ind : int):
        '''
        makes R[`ind`] a pivot 1 by scalar multiplying R[`ind`]
        '''
        col_vals = self.matrix.get_col_values(ind)
        # check if there is a row with a 1 in this column
        # if there is, then swap this row with R[`ind`]
        if 1 in col_vals and self.matrix.get_entry_value_from_row_col(ind,ind) != 1:
            self.matrix.swap_rows(col_vals.index(1), ind)
            return

        self.scalar_multiply_row(
            row=ind,
            scalar=1/(self.get_entry_value_from_row_col(ind,ind)))

    def swap_rows_with_zeros(self, col : int):
        '''
        checks C[col] for entries containing zeros. 
        if there are rows with zeros in the col then put these at the bottom
        '''
        if 0 not in self.matrix.get_col_values(col):
            return None

        while True:

            rows_with_zeros = [row for row in self.matrix.row_indices if self.matrix.get_index_of_first_nonzero_in_row(row) > col]
            rows_without_zero = [row for row in self.matrix.row_indices if row not in rows_with_zeros]

            if min(rows_with_zeros) > max(rows_without_zero):
                # all rows with zeros are lower than rows with non-zeros
                break

            # there is a row with a leading zero above a row without a leading zero
            self.swap_rows(min(rows_with_zeros),max(rows_without_zero))

        
#   ===========================
#   Forward Elimination
#   ===========================

    def make_other_rows_zero_in_col(self, col : int):
        '''
        takes a column index with a pivot 1.
        uses defined row operations to make all non-pivot rows have 0 in the column
        '''
        # find row index containing pivot 1
        pivot_ind = self.get_pivot_index_from_list(self.matrix.get_col_values(col))
        for row in self.matrix.row_indices:
            if row == pivot_ind:
                continue
            self.matrix.subtract_multiple_of_row(
                row_being_subtracted_from=row,
                row_to_subtract=pivot_ind,
                multiple=self.matrix.get_entry_value_from_row_col(row, col)
                )




#   ===========================
#   Back Substitution
#   ===========================


#   ===========================
#   Solve Linear Systems
#   ===========================

    def solve_gaussian(self):
        '''
        ds
        '''
        for i in self.matrix.row_indices:
            # get all rows with zero entries in first col at the bottom
            self.swap_rows_with_zeros(i)
            # make pivot 1 in column
            self.make_pivot_in_col(i)
            # make all other entries in col = 0
            self.make_other_rows_zero_in_col(i)

a = Matrix('A', np.array(A_VALS).reshape(5,5))
b = Matrix('b',np.array(B_VALS).reshape(5,1))
a.augment(b)

g_elim = GaussianElimination(a)
print(g_elim.matrix)
g_elim.solve_gaussian()



# g_elim.make_pivot_in_col(0)
# print(g_elim.augmented)
# g_elim.make_other_rows_zero_in_col(0)
# print(g_elim.augmented)


# Swap rows such that the rows with the most leading zeros are at the bottom
make_leading_zeros_at_bottom(matrix, below_row : int)
    # If there is a RiC1 = 1: swap this Ri with R1
    # Else: divide R1 by it's first coefficient (R1C1)

# Now the matrix has a leading 1 in R1C1 and all zero entries in C1 are at the bottom
# Subtract RiCj*R1Cj from the rows beneath
# Now there is a 1 in R1C1 and all other entries in C1 are zero
# Do the same again for C2:
    make_pivot_one(matrix, row_index_to_make_pivot_one : int)
    subtract_from_rows_beneath(matrix, row_index_to_subtract : int)
# This continues until all rows are in REF
    