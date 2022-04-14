from binary_operation import to_binary, to_string
from hamming_conversion import hamming_decode, hamming_encode
# from table import Presentation


def text_2_hamming(text, parity):
    encoded_string = []
    bin = to_binary(text)
    for index, letter in enumerate(bin):
        print(f"Lettre a encoder : {text[index]}")
        print(f"Binaire à encoder : {parity}{letter}")
        text_encode = hamming_encode(letter, parity)
        print(f"Bits encodé aves la methode Hamming : {text_encode}")
        encoded_string.append(text_encode)
    return encoded_string


def hamming_2_text(encoded_string):
    decoded_string = []
    for binary in encoded_string:
        print(f"Binaire a decoder : {binary}")
        decoded_bytes = hamming_decode(binary)
        print(f"Bits decodé aves la methode Hamming : {decoded_bytes}")
        text_decode = to_string(decoded_bytes).replace("\x00", "")
        print(f"Binaire décodé : {repr(text_decode)}")
        decoded_string.append(text_decode)
    return decoded_string


def main():
    TEXT = "abc"
    print(f"{'-' * 50}\nTexte a encoder : {repr(TEXT)}\n{'-' * 50}")
    encoded_string = text_2_hamming(TEXT, 1)
    print(f"{'-' * 50}\nTexte encodé : {encoded_string}\n{'-' * 50}")
    decoded_string = repr(''.join(hamming_2_text(encoded_string)))
    print(f"{'-' * 50}\nTexte decodé : {decoded_string}\n{'-' * 50}")
    print(
        "Le texte décodé est il identique au texte initial ? {}".format(
                'Oui' if repr(TEXT) == decoded_string else 'Non'
            )
        )
    input("Prenons le cas de données corrompu : ")
    #          'abc' => ['011000000110', '011000011000', '011000011111']
    # corrupted_data => ['011000001110', '011000010000', '011000010111']
    corrupted_data = ["011000001110", "011000010000", "011000010111"]
    print(f"{'-' * 50}\nTexte encodé :\t\t{encoded_string}")
    print(f"Texte encodé corrompu : {corrupted_data}\n{'-' * 50}")
    decoded_string2 = repr(''.join(hamming_2_text(corrupted_data)))
    print(f"{'-' * 50}\nTexte decodé : {decoded_string2}\n{'-' * 50}")
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
