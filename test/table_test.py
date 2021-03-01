from table import Table

import unittest


class TestTable(unittest.TestCase):

    def __init__(self):
        self.user = Table()

    def test_add_player(self):
        raise NotImplementedError


if __name__ == '__main__':
    unittest.main()
