import numpy as np

#             =====================================
#             GPT generated list of numpy functions
#             =====================================
            # Creating and storing matrices
    # np.array()	                    Create an array from a list
    # np.zeros((m, n))	                Create an \(m\times n\) zero matrix
    # np.ones((m, n))	                Create a matrix of ones
    # np.eye(n)	                        Create an \(n\times n\) identity matrix
    # np.empty((m, n), dtype=object)	Allocate an array for your Entry objects
    # np.copy()	                        Copy an array without modifying the original
    # np.reshape()	                    Change array dimensions

            # Accessing and modifying entries
    # A[i, j]	                        Access entry at row i, column j
    # A[i, :]	                        Access an entire row
    # A[:, j]	                        Access an entire column
    # A.shape	                        Get matrix dimensions
    # A.size	                        Number of elements
    # A.dtype	                        Data type of the array
    # A.T	                            Transpose a matrix
    # A.astype()	                    Convert entries to another data type
    # np.concatenate()	                Append rows or columns

            # Gaussian elimination
    # A[[i, j]] = A[[j, i]]	            Swap two rows
    # A[i] *= scalar	                Multiply a row by a scalar
    # A[i] -= scalar * A[j]	            Subtract a multiple of another row
    # np.argmax()	                    Find index of largest value (pivot selection)
    # np.abs()	                        Absolute values for partial pivoting
    # np.isclose()	                    Compare floating-point values approximately
    # np.allclose()	                    Compare entire matrices approximately

            # Linear algebra and testing
    # np.linalg.solve(A, b)	            Verify your solver
    # np.linalg.det(A)	                Calculate determinant
    # np.linalg.matrix_rank(A)	        Calculate matrix rank
    # np.linalg.inv(A)	                Calculate inverse
    # np.matmul(A, B) or A @ B	        Matrix multiplication
    # np.dot()	                        Dot product

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

A_NP_MATRIX = np.array(A_VALS).reshape(5, 5)
B_NP_MATRIX = np.array(B_VALS).reshape(5,1)

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
        self.name = [self.row, self.col]

#   ===========================
#   Properties
#   ===========================

    @property
    def type(self) -> type:
        '''
        returns type of value
        '''
        return type(self.value)

    @property
    def is_zero(self) -> bool:
        '''
        returns true if value is 0
        '''
        return self.value == 0

    @property
    def is_integer(self) -> bool:
        return self.type == int

    @property
    def is_positive(self) -> bool:
        return self.value > 0

    @property
    def is_pivot(self) -> bool:
        return self.row == self.col

    @property
    def magnitude(self) -> float:
        '''
        returns abs(self.value)
        '''
        return abs(self.value)

class Matrix:
    '''
    stores a np.array of entries and gives operations to perform on them as a matrix.
    '''

#   ===========================
#   Properties
#   ===========================

    @property
    def dimensions(self):
        return self.data.shape

    @property
    def matrix(self) -> np.array:
        '''
        docstring
        '''
        mat = []
        for i in range(self.num_rows):
            get_row_values = []
            for j in range(self.num_cols):
                get_row_values.append(self.values[self.get_entry_index(i,j)])
            mat.append(get_row_values)
        return mat

    @property
    def num_rows(self) -> int:
        return self.dimensions[0]

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

    def __init__(
            self,
            name : str,
            values
            ):
        self.name = name
        self.data = np.array(values, dtype=float)
        if self.data.ndim != 2:
            raise ValueError(f"Matrix must be 2 dimensions\n\tDim({self.name}) = {self.data.ndim}")

        self.show_dp = 2
    
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
        s = f"{self.name} is a {self.num_rows}x{self.num_cols} matrix"
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

    def swap_rows(
            self,
            row1 : int,
            row2 : int
            ):
        '''
        swaps two rows
        '''
        self.data[[row1,row2]] = self.data[[row2,row1]]

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

#   ===========================
#   Other Matrix Operations
#   ===========================

    def scalar_multiply_matrix(
            self,
            scalar : float
        ):
        '''
        multiplies every entry in matrix by scalar value
        '''
        self.data *= scalar

    def append_col(
            self,
            new_vals : np.array
        ):
        '''
        docstring
        '''
        if len(new_vals) != self.num_rows:
            raise ValueError(
                f"ERROR: Number of rows in `new_vals` is not equal to number of rows in matrix\n\t(New) {len(new_vals)} != {self.num_rows} ({self.name})"
                )

        np.concatenate(self.data,new_vals)

class GaussianElimination(Matrix):
    '''
    algorithms for Guassian Elimination operations on a Matrix
    '''

#   ===========================
#   Pivot Selection
#   ===========================

    def __init__(
            self,
            name : str,
            entries : list[Entry],
            dimensions : tuple
            ):
        super().__init__(name, entries, dimensions)


#   ===========================
#   Pivot Selection
#   ===========================


#   ===========================
#   Forward Elimination
#   ===========================


#   ===========================
#   Back Substitution
#   ===========================


#   ===========================
#   Solve Linear Systems
#   ===========================


a = Matrix('A', A_NP_MATRIX)
b = Matrix('b', B_NP_MATRIX)
print(a)
print(b)
