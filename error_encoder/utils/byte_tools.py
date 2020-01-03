from typing import List, Union
from functools import partial

bin_to_int = partial(int, base=2)


def is_parity_bit(binary: Union[bytearray, bytes]) -> bool:
    return bin_to_int(binary) & bin_to_int(binary) - 1 == 0


def b_range(stop: int) -> List[bytes]:
    for integer in range(stop):
        yield bin(integer)


if __name__ == '__main__':
    test = []

    for i in range(5):
        parity = 2**i
        result = is_parity_bit(bin(parity))
        test.append(result)

        if result is False:
            print(parity, ' yielded false!')
