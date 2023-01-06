# Active Directory

Most of the operations to this problem take **O(n)** since we are dealing with Python lists most of time.

A user may be or may be not inside a group, if it is then we return True or False otherwise.

We also can look for a user into a group inside the given group, as a matter of fact, we could have used the same queue system used in problem 2 when leading with directories. Since the provided initial code used python lists then we maintained it. The problem can turn into a pretty complexity problem if we create a deep relationship of groups inside groups inside... and so on.

In this worst case some adjustments can be done leading to a time complexity of **O(n+m)** where **n** is the number of groups and **m** is the number of users.
