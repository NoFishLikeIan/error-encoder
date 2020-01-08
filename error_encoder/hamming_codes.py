import numpy as np

from utils import hamming_matrices, byte_tools, matrix_tools


def composite_encoder(message: np.array):
    # TODO: Improve for length different then 4 and 7

    length = message.shape[0]
    rem = 4 - length % 4
    m = length + rem
    splits = int(m/4)

    compounded = np.zeros(m, dtype=int)
    compounded[rem:] = message

    encoded = np.zeros(splits*7, dtype=int)
    for s, msg in enumerate(np.split(compounded, splits)):
        index = s*4
        encoded[index:index+7] = encode(msg)

    return encoded


def composite_decoder(encoded: np.array, msg_len: int):
    splits = int(encoded.shape[0] / 7)

    decoded = np.zeros(msg_len*splits, dtype=int)

    for s, encoded_msg in enumerate(np.split(encoded, splits)):
        index = s*4
        dec = decode(encoded_msg, msg_len)
        decoded[index:index+4] = dec

    return decoded


@matrix_tools.GF(2)
def encode(message: np.array):
    msg_len = message.shape[0] - 1

    _, G = hamming_matrices.matrices_from_m(msg_len)

    codeword = message @ G

    return codeword


@matrix_tools.GF(2)
def decode(encoded: np.array, msg_len: int):
    # TODO: The msg_len is not necessary, it can be derived from the encoded message.
    m = msg_len - 1
    H, _ = hamming_matrices.matrices_from_m(m)

    syndrome = H @ encoded
    is_valid = matrix_tools.is_zero(syndrome)

    if is_valid:
        return encoded[:m+1]

    else:
        error_bit = np.mod(byte_tools.bitvec_to_int(syndrome), msg_len)
        corrected = encoded.copy()
        corrected[error_bit] = encoded[error_bit] + 1

        return corrected[:m+1]


if __name__ == '__main__':
    long_binary_message = np.random.randint(2, size=40)

    encoded = composite_encoder(long_binary_message)
    decoded = composite_decoder(encoded, 4)
