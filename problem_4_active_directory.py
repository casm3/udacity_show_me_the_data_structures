class Group(object):
    def __init__(self, _name):
        self.name = _name
        self.groups = []
        self.users = []

    def add_group(self, group):
        self.groups.append(group)

    def add_user(self, user):
        self.users.append(user)

    def get_groups(self):
        return self.groups

    def get_users(self):
        return self.users

    def get_name(self):
        return self.name


def is_user_in_group(user, groups):
    """
    Return True if user is in the group, False otherwise.

    Args:
      user(str): user name/id
      group(class:Group): group to check user membership against
    """
    if user in groups.get_users() and type(groups) == Group:
        return True

    for group in groups.get_groups():
        if user in group.get_users():
            return True
    return False


# Add your own test cases: include at least three test cases
# and two of them must include edge cases, such as null, empty
# or very large values


parent = Group("parent")
child = Group("child")
brother = Group("brother")

child_user = "child_user"
child.add_user(child_user)

brother_user = "brother_user"
brother.add_user(brother_user)

parent.add_group(child)
parent.add_group(brother)

# Test Case 1
assert is_user_in_group("child_user", child)
# Test Case 2
assert is_user_in_group("fail_test_case", brother) is False
# Test Case 3
assert is_user_in_group("child_user", parent)
