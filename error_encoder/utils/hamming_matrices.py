from typing import Tuple

import numpy as np

from .byte_tools import int_to_bitvec
from .matrix_tools import systematize_matrix, reverse_permutation


def dimensions_hamming(m: int) -> Tuple[int, int]:
    """
    Takes the "m" value and returns (n, k) for the Hamming matrix

    """

    n = np.power(2, m) - 1
    k = n-m

    return n, k


def generate_H(n: int, k: int) -> np.array:
    """
    Constructs the H matrix with:
    - n rows
    - (n-K) columns
    """

    c = n-k
    H = np.zeros((n, c))

    for row in range(n):
        binary_rap = int_to_bitvec(row + 1, length=c)
        H[row] = binary_rap

    return H.T


def systematize_algorithm(H: np.array) -> Tuple[np.array, np.array, np.array]:
    """
    Construct the systematic rapresentations of G and H, as well as the G matrix based on the H matrix.
    """
    n, c = H.shape
    m = np.abs(n-c)

    G_s = np.zeros((m, c))
    G_s[:, :m] = np.identity(m)

    H_s, permutation = systematize_matrix(H, post_system=True)

    rev_permutation = reverse_permutation(permutation)

    P = H_s[:, :m]

    G_s[:, m:] = P.T

    G = G_s[:, rev_permutation]

    return G, G_s, H_s
