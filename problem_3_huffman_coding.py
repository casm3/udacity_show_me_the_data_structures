from collections import Counter
import sys


class Node:
    def __init__(
        self,
        letter_count,
        letter,
        left_child=None,
        right_child=None
    ):
        self.letter_count = letter_count
        self.letter = letter
        self.left_child = left_child
        self.right_child = right_child
        self.code = ""


def calculate_codes(node: Node, encoded_data='', codes=dict()):
    updated_value = encoded_data + str(node.code)

    if not node.left_child and not node.right_child:
        codes[node.letter] = updated_value
    else:
        calculate_codes(node.left_child, updated_value, codes)
        calculate_codes(node.right_child, updated_value, codes)

    return codes


def huffman_encoding(data: str):
    letters_count = Counter(data)
    letters: list[str] = letters_count.keys()

    nodes = [Node(letters_count.get(letter), letter) for letter in letters]

    while len(nodes) > 1:
        nodes = sorted(nodes, key=lambda x: x.letter_count)

        right, left = nodes[0], nodes[1]

        left.code, right.code = 0, 1

        nodes.remove(left)
        nodes.remove(right)
        nodes.append(
            Node(
                left.letter_count+right.letter_count,
                left.letter+right.letter,
                left,
                right
            )
        )

    huffman_encoding = calculate_codes(nodes[0])
    encoded_output = [huffman_encoding[letter] for letter in data]
    return "".join(encoded_output), nodes[0]


def huffman_decoding(data: str, tree):
    root = tree
    decoded_output = []
    for boolean in data:
        if boolean == '1':
            tree = tree.right_child
        else:
            tree = tree.left_child

        try:
            if not tree.left_child.letter and not tree.right_child.letter:
                continue
        except AttributeError:
            decoded_output.append(tree.letter)
            tree = root

    return "".join([str(letter) for letter in decoded_output])


if __name__ == "__main__":
    codes = {}

    a_great_sentence = "The bird is the word"

    print(f"The size of the data is: {sys.getsizeof(a_great_sentence)}\n")
    print(f"The content of the data is: {a_great_sentence}\n")

    encoded_data, tree = huffman_encoding(a_great_sentence)

    print(f"The size of the encoded data is: \
        {sys.getsizeof(int(encoded_data, base=2))}\n")
    print(f"The content of the encoded data is: {encoded_data}\n")

    decoded_data = huffman_decoding(encoded_data, tree)

    print(f"The size of the decoded data is: {sys.getsizeof(decoded_data)}\n")
    print(f"The content of the encoded data is: {decoded_data}\n")

# Test cases
udacity = "Udacity"
huffman = "huffman"
# Code based on the implementation provided by Yağmur Çiğdem Aktaş
source = "https://towardsdatascience.com/huffman-decoding-cca770065bab"

encoded_data, tree = huffman_encoding(udacity)
assert huffman_decoding(encoded_data, tree) == udacity

encoded_data, tree = huffman_encoding(huffman)
assert huffman_decoding(encoded_data, tree) == huffman

encoded_data, tree = huffman_encoding(source)
assert huffman_decoding(encoded_data, tree) == source
