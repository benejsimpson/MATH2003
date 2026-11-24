import numpy as np
from time import perf_counter_ns

flong = np.float64
fvec = list[flong]
fmat = list[list[flong]]
ROUNDING_DP = 3

class Entry:
    '''
    Representation of an entry in a matrix
    '''
    def __init__(
            self,
            value : flong):
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
        change global `ROUNDING_DP` to change number of dp
        '''
        return round(self.value, ROUNDING_DP)

class Row:
    '''
    Represents a row of a matrix. takes a list of floats, stores as a list of Entry objects.
    '''
    def __init__(
            self,
            entries : list[flong],
            row_index : int,
            is_augmented : bool = False
            ):
        self.entries = [Entry(entry) for entry in entries]
        self.is_augmented = is_augmented
        self.row_index = row_index

    @property
    def length(self):
        '''
        number of entries in row
        '''
        return len(self.entries)

    @property
    def first_non_zero_index(self):
        '''
        returns index of first non-zero entry in row. Returns None if all entries are zero
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
        returns value of first non-zero entry in row. Returns None if all entries are zero
        '''
        ind = self.first_non_zero_index
        if ind is None:
            return None
        return self.entries[self.first_non_zero_index].value

    def scalar_multiply_row(self, scalar : flong):
        '''
        Multiplies each entry in row by a scalar float
        '''
        for val in self.entries:
            val.scalar_multiply(scalar)

    def subtract_multiple_of_row(self, row_to_subtract : Row, scalar : flong):
        '''
        iterates through each entry in row and subtracts scalar multiple of each entry in `row_to_subtract`
        '''
        for i,entry in enumerate(self.entries):
            entry.subtract_multiple_of_entry(row_to_subtract.entries[i], scalar)

    def update_row_index(self, new_index : int):
        '''
        updates the row index. used for swapping rows
        '''
        self.row_index = new_index

    def __str__(self) -> str:
        s = ""
        for entry in self.entries:
            s += f"{round(entry.value, ROUNDING_DP)}\t"
        s += f"length : {self.length}\tAugmented : {self.is_augmented}"
        return s

class Matrix:
    '''
    Representation of a matrix. takes input as list containing lists of rows of floats.\n
    Matrix operations to perform for gaussian elimination algorithm
    '''
    def __init__(
            self,
            rows : fmat,
            is_augmented : bool = False
            ):
        self.rows = [Row(entries,i,is_augmented) for i,entries in enumerate(rows)]
        self.is_augmented = is_augmented

    def __str__(self) -> str:
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
        dim(A)
        '''
        if not self.is_valid:
            return None
        return len(self.rows),self.rows[0].length

    @property
    def num_rows(self):
        '''
        dim(A)[0]
        '''
        return self.dimensions[0]

    @property
    def augmented_values(self):
        '''
        if the matrix is augmented, returns list of values in the augmented column
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

    def print_system(self):
        '''
        prints the system of equations in terminal. if augmented then has = `val`
        '''
        st = "\n"
        num_vars = self.rows[0].length
        if self.is_augmented:
            num_vars -= 1
            aug_vals = self.augmented_values

        for row_ind, row in enumerate(self.rows):
            strow = ""
            for i in range(num_vars):
                strow += f"{row.entries[i].value} x{i+1}"
                if i != num_vars-1:
                    strow += " + "
            if self.is_augmented:
                strow += f" = {aug_vals[row_ind]}"
            st += f"{strow}\n"
        print(st)

class GaussianElimination:
    '''
    Algorithm for Gaussian elimination
    '''
    def __init__(self, matrix : Matrix):
        self.matrix = matrix
        self.num_rows = matrix.num_rows
        self.is_augmented = matrix.is_augmented

    def __str__(self):
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
        puts matrix into row-echolon form
        '''
        for col in range(self.num_rows):
            self.make_pivot_column(col)

    def augmented_values(self, show_dp : int = 3):
        '''
        returns list of values in augmented column.
        '''
        return [round(val,show_dp) for val in self.matrix.augmented_values]

    def back_substitution(self):
        '''
        performs back-substitution on a matrix in REF to solve variables.
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
    A.print_system()
    algo = GaussianElimination(A)

    algo.make_REF()
    algo.back_substitution()

    xs = algo.augmented_values()
    res = "Solutions to variables: \n"
    for i,x in enumerate(xs):
        res += f"x{i+1} = {x}, "
    print(res,'\n')
    return xs

def perf():
    '''
    returns the average time taken (ns) to solve system of equations using `GaussianElimination` over 10 000 repetitions
    '''
    res = []

    for _ in range(10000):
        A = Matrix(rows=A_VALS)
        A.augment_matrix(vector=B_VALS)
        algo = GaussianElimination(A)

        start = perf_counter_ns()

        algo.select_pivot_row(0)
        algo.make_REF()
        algo.back_substitution()

        end = perf_counter_ns()
        res.append(end-start)

    return sum(res)/len(res)

def np_check(
        matrix : fmat,
        vector : fvec
        ) -> fvec:
    '''
    takes matrix A and vector b. checks that my solution matches NumPy's
    '''
    A = np.array(matrix, dtype=float)
    b = np.array(vector, dtype=float).reshape(-1)

    x_numpy = np.linalg.solve(A, b)
    x_mine = np.asarray(run(matrix, vector)).reshape(-1)

    print("My solution:   ", x_mine)
    print("NumPy solution:", x_numpy)
    print("Solutions agree:", np.allclose(x_mine, x_numpy, rtol=1e-8, atol=1e-10))
    print("Residual A @ x - b:", A @ x_mine - b)

if __name__ == '__main__':
    # Uncomment lines to run

    run(A_VALS, B_VALS)
    # print(f"Average run-time: {perf()} ns\n")
    # np_check(A_VALS,B_VALS)
