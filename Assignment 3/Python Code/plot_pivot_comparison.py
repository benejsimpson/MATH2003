"""Run with Python 3.14 alongside the two original solver files."""
from pathlib import Path
from runpy import run_path

import matplotlib.pyplot as plt
import numpy as np

from GPT_generated_guassian_elimination_algorithm import gaussian_elimination

HERE = Path(__file__).resolve().parent


def solve_with_bens_code(A, b):
    # The extra dot in Assignment_3.2.py prevents a normal import.
    module = run_path(str(HERE / "Assignment_3.2.py"))
    matrix = module["Matrix"](rows=A.tolist())
    matrix.augment_matrix(vector=b.tolist())
    solver = module["GaussianElimination"](matrix)
    solver.make_REF()
    solver.back_substitution()
    # The run() wrapper prints rounded answers. Read the raw solution instead.
    return np.asarray(matrix.augmented_values)


def no_swap_example(A, b):
    """One elimination step and back substitution for this 2-by-2 control."""
    multiplier = A[1, 0] / A[0, 0]
    y = (b[1] - multiplier * b[0]) / (A[1, 1] - multiplier * A[0, 1])
    x = (b[0] - A[0, 1] * y) / A[0, 0]
    return np.array([x, y])


def main():
    epsilon = 1e-16
    A = np.array([[epsilon, 1.0], [1.0, 1.0]])
    b = np.array([1.0 + epsilon, 2.0])
    solutions = {
        "No row swap (control)": no_swap_example(A, b),
        "My solver": solve_with_bens_code(A, b),
        "ChatGPT solver": gaussian_elimination(A, b),
        "NumPy solve": np.linalg.solve(A, b),
    }

    fig, ax = plt.subplots(figsize=(6.4, 2.4), layout="constrained")
    ax.axvline(1, color="0.65", linestyle="--", linewidth=1, zorder=0)
    for row, (name, (x, y)) in enumerate(solutions.items()):
        print(f"{name:24s} x = {x:.17g}    y = {y:.17g}")
        ax.plot(x, row, "o", color="#244a68")
        ax.annotate(f"{x:.5g}", (x, row), xytext=(7, 0),
                    textcoords="offset points", va="center")

    ax.set_yticks(range(len(solutions)), labels=list(solutions))
    ax.set_ylim(len(solutions) - 0.5, -0.5)
    ax.set_xlim(0, 2.65)
    ax.set_xlabel("Computed value of x (exact value = 1)")
    ax.spines[["top", "right", "left"]].set_visible(False)
    ax.tick_params(axis="y", length=0)
    fig.savefig(HERE / "pivot_comparison.pdf")
    plt.show()


if __name__ == "__main__":
    main()
