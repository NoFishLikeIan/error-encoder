from typing import List

import numpy as np

from functools import wraps


def non_zero(column_vector) -> int:
    """
    Returns position of non-zero element assuming there is one.
    """
    return np.nonzero(column_vector)[0][0]


def reverse_permutation(perm: List[int]) -> List[int]:
    rev_perm = [-1]*len(perm)
    for index, mapping in enumerate(perm):
        rev_perm[mapping] = index

    return rev_perm


def systematize_matrix(M: np.array, post_system=False) -> np.array:

    # TODO: Check for repeated identity matrix columns
    m, _ = M.shape

    id_perm = [np.inf]*m
    non_id_perm = []

    for index, column in enumerate(M.T):
        if np.sum(column) != 1:
            non_id_perm.append(index)
        else:
            idx_id = non_zero(column)
            id_perm[idx_id] = index

    if np.sum(id_perm) < np.inf:

        permutation = non_id_perm + id_perm if post_system else id_perm + non_id_perm

        M_s = M[:, permutation]

        return M_s, permutation

    else:
        raise ValueError("Could not find identity matrix in", M)


def GF(m):

    def callable(numpy_fn):
        @wraps(numpy_fn)
        def modded(*args, **kwargs):
            R = numpy_fn(*args, **kwargs)
            return np.mod(R, m)

        return modded

    return callable


def is_zero(matrix):
    mod = np.mod(matrix, 2)
    return not np.any(mod)
