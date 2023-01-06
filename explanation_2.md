# File Recursion

A double ended queue (deque) was selected here.

All directories are added to this queue longside with the files inside these directories. As long as there is a directory, we extract all files in this directory and add them to the queue.

Once there is nothing inside the queue we have checked all files in all directories.

A deque was selected due to the fact that we can push and pop values in O(1). As for general time complexity we have O(f+d) where __f__ is the amount of files and __d__ is the amount of directories to be added and removed to the queue.

In order to run the tests for this problem you need to run `python3 -m unittest`.
