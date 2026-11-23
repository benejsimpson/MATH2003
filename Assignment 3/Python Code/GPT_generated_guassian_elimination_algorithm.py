import numpy as np


def gaussian_elimination(A, b):
    """Solve a dense square system using Gaussian elimination with partial pivoting.

    A shape (n,) or (n, 1) right-hand side gives x with the same shape.
    Inputs are copied. A zero pivot after pivot selection raises ValueError.
    """
    A = np.asarray(A)
    b = np.asarray(b)
    if A.ndim != 2 or A.shape[0] != A.shape[1]:
        raise ValueError("A must be square.")
    n = A.shape[0]
    if b.shape not in ((n,), (n, 1)):
        raise ValueError("b must have shape (n,) or (n, 1).")
    if A.dtype.kind not in "biufc" or b.dtype.kind not in "biufc":
        raise TypeError("A and b must contain numbers.")

    dtype = np.result_type(A.dtype, b.dtype, np.float64)
    rows = np.empty((n, n + 1), dtype=dtype)
    rows[:, :n] = A
    rows[:, n] = b.reshape(n)
    if not np.isfinite(rows).all():
        raise ValueError("A and b must be finite.")

    # Reuse a small block of storage for the scaled pivot rows.
    block_size = 32
    work = np.empty((min(block_size, n), n), dtype=dtype)
    for k in range(n):
        pivot = k + np.argmax(np.abs(rows[k:, k]))
        if rows[pivot, k] == 0:
            raise ValueError("Zero pivot after row selection. No unique solution.")
        if pivot != k:
            rows[[k, pivot], k:] = rows[[pivot, k], k:]

        # The eliminated column can hold the multipliers until this step ends.
        rows[k + 1:, k] /= rows[k, k]
        for start in range(k + 1, n, block_size):
            end = min(start + block_size, n)
            scaled = work[:end - start, :n - k]
            np.multiply(rows[start:end, k:k + 1], rows[k, k + 1:], out=scaled)
            rows[start:end, k + 1:] -= scaled

    x = np.empty(n, dtype=dtype)
    for k in range(n - 1, -1, -1):
        known = np.sum(rows[k, k + 1:n] * x[k + 1:])
        x[k] = (rows[k, n] - known) / rows[k, k]
    return x.reshape(b.shape)
