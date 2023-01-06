# Blockchain

For the Blockchain problem we reused the code provided by Udacity for LinkedLists and Block structures.

We may add an element to a linked list in **O(1)**, I had also improved the implementation by adding a search by block, the search returns the hash for the given block if this block is in the linked list, this operation takes **O(n)**.

It is important to mention that the data for a block was the field chosen to be hashed, but the given block once encoded could also be hashed and I think that this could be a better approach.

The general complexity is O(n).
