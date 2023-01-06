# Union and Intersection

Here an approach based on extracting the values of the linked lists to a python's set data structure provided the best approach. Then we applied either union or intersection built-in set functions. So the time complexity here for the union operation is **O(n+k)**, where **n** is the size of the first linked list and **k** the size for the second linked list.

Finally, for the intersection approach we have a **O(min(n, k))**, or Big O of the minimum size between linked list 1 and linked list 2.

After doing the operations (union and intersection) we created and returned a new linked list with the operation result(O(n) approach).
