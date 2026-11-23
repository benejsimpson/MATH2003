import numpy as np
flong = np.float64
fvec = list[flong]
fmat = list[list[flong]]
ROUNDING_DP = 3

class Entry:
    '''
    DocString
    '''
    def __init__(
            self,
            value : flong):
        '''
        DocString
        '''
        self.value = value

    def scalar_multiply(self, scalar : flong):
        '''
        multiplies entry value by a scalar
        '''
        self.value *= scalar

    def subtract_multiple_of_entry(self, entry : Entry, scalar : flong):
        '''
        subtracts a multiple of another entry's value from this entry's value
        '''
        self.value -= (entry.value * scalar)

    def __str__(self) -> str:
        '''
        DocString
        '''
        return round(self.value, ROUNDING_DP)

class Row:
    '''
    DocString
    '''
    def __init__(
            self,
            entries : list[flong],
            row_index : int,
            is_augmented : bool = False
            ):
        '''
        DocString
        '''
        self.entries = [Entry(entry) for entry in entries]
        self.is_augmented = is_augmented
        self.row_index = row_index

    @property
    def length(self):
        '''
        DocString
        '''
        return len(self.entries)

    @property
    def first_non_zero_index(self):
        '''
        DocString
        '''
        l = self.length
        if self.is_augmented:
            l -= 1
        for i in range(l):
            if self.entries[i].value != 0:
                return i
        return None

    @property
    def first_non_zero_value(self):
        '''
        DocString
        '''
        ind = self.first_non_zero_index
        if ind is None:
            return None
        return self.entries[self.first_non_zero_index].value

    def scalar_multiply_row(self, scalar : flong):
        '''
        DocString
        '''
        for val in self.entries:
            val.scalar_multiply(scalar)

    def subtract_multiple_of_row(self, row_to_subtract : Row, scalar : flong):
        '''
        DocString
        '''
        for i,entry in enumerate(self.entries):
            entry.subtract_multiple_of_entry(row_to_subtract.entries[i], scalar)

    def update_row_index(self, new_index : int):
        '''
        DocString
        '''
        self.row_index = new_index

    def __str__(self) -> str:
        '''
        DocString
        '''
        s = ""
        for entry in self.entries:
            s += f"{round(entry.value, ROUNDING_DP)}\t"
        s += f"length : {self.length}\tAugmented : {self.is_augmented}"
        return s

class Matrix:
    '''
    DocString
    '''
    def __init__(
            self,
            rows : fmat,
            is_augmented : bool = False
            ):
        '''
        DocString
        '''
        self.rows = [Row(entries,i,is_augmented) for i,entries in enumerate(rows)]
        self.is_augmented = is_augmented

    def __str__(self) -> str:
        '''
        DocString
        '''
        s = ""
        for row in self.rows:
            s += f"{str(row)}\n"
        return s

    @property
    def is_valid(self) -> bool:
        '''
        checks that all rows are same length.\n
        raises ValueError if not.
        '''
        l = self.rows[0].length
        for row in self.rows[1:]:
            if row.length != l:
                raise ValueError (f"Dimensions are wrong.\n{self.__str__()}")
        return True

    @property
    def dimensions(self) -> list[int]:
        '''
        DocString
        '''
        if not self.is_valid:
            return None
        return len(self.rows),self.rows[0].length

    @property
    def num_rows(self):
        '''
        DocString
        '''
        return self.dimensions[0]

    @property
    def augmented_values(self):
        '''
        DocString
        '''
        if not self.is_augmented:
            raise LookupError ("Matrix is not augmented")

        return [row.entries[-1].value for row in self.rows]

    def swap_rows(self, row1 : int, row2 : int):
        '''
        swaps two rows.
        '''
        self.rows[row1], self.rows[row2] = self.rows[row2], self.rows[row1]

    def augment_matrix(self, vector : fmat):
        '''
        augments matrix by appending values in vector to each row of matrix.\n
        updates is_augmented for each row and augmented matrix.
        '''
        for i,row in enumerate(self.rows):
            row.entries.append(Entry(vector[i]))
            row.is_augmented = True
        self.is_augmented = True


class GaussianElimination:
    '''
    DocString
    '''
    def __init__(self, matrix : Matrix):
        '''
        DocString
        '''
        self.matrix = matrix
        self.num_rows = matrix.num_rows
        self.is_augmented = matrix.is_augmented

    def __str__(self):
        '''
        DocString
        '''
        return str(self.matrix)

    def select_pivot_row(self, col : int):
        '''
        finds largest abs value in rows[col:] and swaps this into row[col]
        '''
        pivot_ind = max(
            range(col, self.num_rows),
            key=lambda i : abs(self.matrix.rows[i].entries[col].value)
        )
        self.matrix.swap_rows(col,pivot_ind)

    def make_pivot_column(self, col : int):
        '''
        selects pivot row and makes the entry a pivot 1.\n
        subtracts multiples of this row from all rows beneath.
        '''
        self.select_pivot_row(col)
        pivot_row = self.matrix.rows[col]
        pivot_val = pivot_row.entries[col].value

        if pivot_val == 0:
            raise ValueError (f"Found zero in R{col}C{col}")

        pivot_row.scalar_multiply_row(1 / pivot_val)

        for row in self.matrix.rows[col+1:]:
            row.subtract_multiple_of_row(pivot_row, row.entries[col].value)

    def make_REF(self):
        '''
        DocString
        '''
        for col in range(self.num_rows):
            self.make_pivot_column(col)

    def augmented_values(self, show_dp : int = 3):
        '''
        DocString
        '''
        return [round(val,show_dp) for val in self.matrix.augmented_values]

    def back_substitution(self):
        '''
        DocString
        '''
        for i in range(1,self.num_rows):
            # find the value in the corresponding row of the augmented column
            known_value = self.matrix.rows[self.num_rows-i].entries[-1].value
            # loop through all rows above
            for row in self.matrix.rows[:-i]:
                # subtract (coefficient * known variable) from row of augmented column
                row.entries[-1].subtract_multiple_of_entry(
                    row.entries[-i-1],
                    known_value
                )
                # now the known variable has been eliminated, set the coefficient to zero
                row.entries[-i-1].value = 0


A_VALS = [
    [-1.5,  2.3,  0.3,  0.3,  0.5],
    [-1.4,  1.5,  2.1, -0.2, -1.6],
    [-0.1, -0.3,  2.3,  0.9,  0.4],
    [0.6,  0.8,  1.7, -2.4,  1.7],
    [-0.2,  0.4, -0.2,  1.1, -0.9]
]
B_VALS = [
    -7.7,
    -13.9,
    -34.4,
    -43.5,
    12
]

def run(
        matrix : fmat,
        vector : fvec
        ) -> fvec:
    '''
    Takes 2 inputs:\n
    - nxn matrix representing system of equations. Each row_i contains a_ij for j = 1,2,...,n :\n\t
    a_11 * x_1 + a_12 * x_2 + ... + a_1n * x_n\n\t
    a_21 * x_1 + a_22 * x_2 + ... + a_2n * x_n\n\t
    ...\n\t
    a_n1 * x_1 + a_n2 * x_2 + ... + a_nn * x_n\n
    - 1xn vector representing result of each equation\n
    Performs 2-step Gaussian elimination:\n
    1. Get system into REF\n
    2. Back-substitute to evauluate unknown variables\n
    Returns the solutions to each variable (x_1,x_2,...,x_n) that satisfy the system of equations.
    '''

    A = Matrix(rows=matrix)
    A.augment_matrix(vector=vector)
    algo = GaussianElimination(A)

    algo.select_pivot_row(0)
    algo.make_REF()
    algo.back_substitution()

    print(algo.augmented_values())

if __name__ == '__main__':
    run(A_VALS,B_VALS)
