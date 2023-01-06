import os
import unittest
from collections import deque


def find_files(suffix=".c", path="testdir"):
    """
    Find all files beneath path with file name suffix.

    Note that a path may contain further subdirectories
    and those subdirectories may also contain further subdirectories.

    There are no limit to the depth of the subdirectories can be.

    Args:
      suffix(str): suffix if the file name to be found
      path(str): path of the file system

    Returns:
       a list of paths
    """
    queue_repository = deque(os.listdir(path))
    list_of_elements = []
    while len(queue_repository):
        popped_element = queue_repository.popleft()
        if "." in suffix and popped_element.endswith(suffix):
            list_of_elements.append(popped_element)
        elif "." in popped_element:
            pass
        else:
            for element in os.listdir(f"{path}/{popped_element}"):
                queue_repository.append(f"{popped_element}/{element}")
    return list_of_elements


# Add your own test cases: include at least three test cases
# and two of them must include edge cases, such as null, empty or very large
# values


class TestFindFiles(unittest.TestCase):
    def test_find_gitkeep(self):
        assert find_files(suffix=".gitkeep") == [
            "subdir4/.gitkeep", "subdir2/.gitkeep"]

    def test_find_c(self):
        assert find_files(suffix=".c") == [
            "t1.c",
            "subdir5/a.c",
            "subdir1/a.c",
            "subdir3/subsubdir1/b.c",
        ]

    def test_find_h(self):
        assert find_files(suffix=".h") == [
            "t1.h",
            "subdir5/a.h",
            "subdir1/a.h",
            "subdir3/subsubdir1/b.h",
        ]

    def test_no_file(self):
        assert find_files(suffix=".wrong") == []

    def test_folder(self):
        assert find_files(suffix="subdir4") == []


if __name__ == "__main__":
    unittest.main()
