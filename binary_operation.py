def zero_bin(binary):
    while len(binary) < 7:
        binary = "0" + binary
    return binary


def toBinary(text):
    ord_list, bin_list = [], []
    for i in text:
        ord_list.append(ord(i))
    for i in ord_list:
        bin_list.append(zero_bin(bin(i)[2:]))
    return bin_list


def toString(bytes):
    binary_int = int(bytes[1:], 2)
    byte_number = binary_int.bit_length() + 7 // 8
    binary_array = binary_int.to_bytes(byte_number, "big")
    ascii_text = binary_array.decode()
    return ascii_text


def zero_rbns(rbns_list):
    max_length = len(max(rbns_list, key=len))
    for i in rbns_list:
        while len(i) < max_length:
            i.insert(0, 0)


def bit_one(bytes):
    return [i + 1 for i, x in enumerate(bytes[::-1]) if x == "1"]


def sum_columns(matrix):
    return [matrix.sum(axis=0)]


def rbns(nbr):
    return list(map(int, list(bin(nbr)[2:])))
