from binary_operation import toBinary, toString
from hamming_conversion import hamming_decode, hamming_encode


def text_2_hamming(bin, parity):
    encoded_string = []
    for letter in bin:
        print(f"Binaire à encoder : {parity}{letter}")
        text_encode = hamming_encode(letter, parity)
        print(f"Bits encodé aves la methode Hamming : {text_encode}")
        encoded_string.append(text_encode)
    return encoded_string


def hamming_2_text(encoded_string):
    decoded_string = []
    for binary in encoded_string:
        decoded_bytes = hamming_decode(binary)
        print(f"Bits decodé aves la methode Hamming : {decoded_bytes}")
        text_decode = toString(decoded_bytes).replace("\x00", "")
        print(f"Binaire décodé : {repr(text_decode)}")
        decoded_string.append(text_decode)
    return decoded_string


def main():
    text = "abc"
    print(f"{'-' * 50}\nTexte a encoder : {repr(text)}\n{'-' * 50}")
    bin = toBinary(text)
    encoded_string = text_2_hamming(bin, 1)
    print(f"{'-' * 50}\nTexte encodé : {encoded_string}\n{'-' * 50}")
    decoded_string = hamming_2_text(encoded_string)
    print(
        "{}\nTexte decodé : {}\n{}".format(
            str('-' * 50),
            repr(''.join(decoded_string)),
            str('-' * 50)
            )
        )
    input("Prenons le cas de données corrompu : ")
    #          'abc' => ['011000000110', '011000011000', '011000011111']
    # corrupted_data => ['011000001110', '011000010000', '011000010111']
    corrupted_data = ["011000001110", "011000010000", "011000010111"]
    print(f"{'-' * 50}\nTexte encodé :\t\t{encoded_string}")
    print(f"Texte encodé corrompu : {corrupted_data}\n{'-' * 50}")
    decoded_string2 = hamming_2_text(corrupted_data)
    print(
        "{}\nTexte decodé : {}\n{}".format(
            str('-' * 50),
            repr(''.join(decoded_string2)),
            str('-' * 50)
            )
        )
    print(
        "Bytes identiques ? {}".format(
            'Oui' if encoded_string == corrupted_data else 'Non'
        )
    )
    print(
        "Résultats identiques ? {}".format(
            'Oui' if decoded_string == decoded_string2 else 'Non'
        )
    )


if __name__ == "__main__":
    main()
