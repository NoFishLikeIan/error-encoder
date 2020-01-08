import numpy as np

from typing import List, Union
from functools import partial

bin_to_int = partial(int, base=2)


def is_parity_bit(binary: Union[bytearray, bytes]) -> bool:
    return bin_to_int(binary) & bin_to_int(binary) - 1 == 0


def b_range(stop: int) -> List[bytes]:
    for integer in range(stop):
        yield bin(integer)


def int_to_bitvec(binary: str, length=None) -> np.array:
    prefix = '' if length is None else f'0{length}'
    binary_string = format(binary, f'{prefix}b')
    return np.array([int(b) for b in binary_string])


def bitvec_to_bitstr(vec: np.array) -> str:
    return ''.join((str(int(i)) for i in vec.tolist())).lstrip('0')


def bitvec_to_int(vec: np.array) -> int:
    vec_gf2 = np.mod(vec, 2)
    stringified = bitvec_to_bitstr(vec_gf2)

    return int(stringified, base=2)


if __name__ == '__main__':
    pass
