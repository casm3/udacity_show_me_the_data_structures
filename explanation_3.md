# Huffman Coding

There are a dozen of **O(n)** operations in this implementation, since we are leading most with text, either literal or numerical strings here. As to update a string we are currently recreating a new one, since python strings are immutable types.

We also combine use of strings with a subtype of dictionaries (Counter), which is created in order to account how many times each character appears on the original string. Most operations in dictionaries takes **O(1)** complexity, but in order to count each character we are dealing here with **O(n)**.

Finally not last, we may reach a general time complexity **O(n*m)** in huffman_decoding. Where **n** is the size of the input string and **m** is the tree size that we may need to loop through entirely.
