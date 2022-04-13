import numpy as np
from binary_operation import zero_rbns, bit_one, sum_columns, rbns


def remove_check(bytes, indexes):
    bytes = bytes[::-1]
    for i in indexes:
        bytes.pop(i - 1)
    return bytes[::-1]


def add_check(bytes, check):
    check_index = 0
    for index, value in enumerate(bytes):
        if value == "control_bit":
            bytes[index] = check[check_index]
            check_index += 1


def modify_wrong_bits(bytes, index):
    bytes = bytes[::-1]
    try:
        bytes[sum(index) - 1] = int(not (int(bytes[sum(index) - 1])))
    except IndexError:
        pass
    return bytes[::-1]


def hamming_decode(encoded_bytes):
    assert (
        len(encoded_bytes) == 12
    )  # 7 bits encodé + 4 bits de controle + 1 bit de parité
    encoded_bytes = list(encoded_bytes)
    # print(*encoded_bytes, sep="")
    parity_bit = encoded_bytes.pop(0)
    # print(parity_bit)
    # print(*encoded_bytes, sep="")
    one_bits = bit_one(encoded_bytes[1:])
    rbns_one_bits = list(map(rbns, one_bits))
    zero_rbns(rbns_one_bits)
    bytes_matrix = np.matrix(rbns_one_bits)
    power_2 = [2**i for i in range(len(np.array(bytes_matrix)[0]))][::-1]
    # print(bytes_matrix)
    sum_matrix_column = sum_columns(np.matrix(bytes_matrix))
    error = []
    for index, value in enumerate(np.array(sum_matrix_column).flatten()):
        if parity_bit == 1:
            if value % 2 == 0:
                error.append(2**index)
        else:
            if value % 2 == 1:
                error.append(2**index)
    # print(sum(error))
    if len(error) != 0:
        encoded_bytes = modify_wrong_bits(encoded_bytes, error)
    decoded_bytes = remove_check(encoded_bytes, power_2)
    decoded_bytes.insert(0, parity_bit)
    return "".join(list(map(str, decoded_bytes)))


def hamming_encode(decoded_bytes, parity):
    decoded_bytes = list(decoded_bytes)
    power_2 = [2**i for i in range(4)]
    for i in power_2:
        decoded_bytes.insert(len(decoded_bytes) - (i - 1), "control_bit")
    pos_of_one = bit_one(decoded_bytes)
    rbns_one_bits = list(map(rbns, pos_of_one))
    zero_rbns(rbns_one_bits)
    bytes_matrix = np.matrix(rbns_one_bits)
    # print(bytes_matrix)
    sum_matrix_column = np.array(
        sum_columns(np.matrix(bytes_matrix))
    ).flatten()
    # print(sum_matrix_column)
    parity_bit = []
    for i in sum_matrix_column:
        if parity == 0:
            if i % 2 == 0:
                parity_bit.append(0)
            else:
                parity_bit.append(1)
        elif parity == 1:
            if i % 2 == 1:
                parity_bit.append(0)
            else:
                parity_bit.append(1)
        else:
            raise ValueError("Parity must be 1 or 0")
    add_check(decoded_bytes, parity_bit)
    return str(parity) + "".join(list(map(str, decoded_bytes)))
