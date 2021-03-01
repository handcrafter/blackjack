from player import User Action

import unittest


class TestUser(unittest.TestCase):

    def __init__(self):
        self.user = User("test_user")

    def test_bet(self):
        user_bet = self.user.bet()
        self.assertEqual(type(user_bet), int)
        self.sssertTrue(user_bet > 0)

    def test_act(self):
        sample_hand = [Card(Suit.DIAMONDS, 1)]
        user_act = self.user.act(sample_hand)
        self.assertTrue('foo'.upper() in Action)


class TestDealer(unittest.TestCase):

    def __init__(self):
        self.user = Dealer("test_dealer")

    def test_bet(self):
        """Dealer bet should be invalid
        """
        self.assertRaises(NotImplementedError, self.user.bet())

    def test_act(self):
        user_act = self.user.act()
        self.assertTrue('foo'.upper() in Action)


if __name__ == '__main__':
    unittest.main()
