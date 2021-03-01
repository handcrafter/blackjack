from blackjack.player import User, Dealer, Action

import unittest


class TestUser(unittest.TestCase):

    def test_bet(self):
        """[summary]
        """
        user = User("test_user")
        user_bet = user.bet()
        self.assertEqual(type(user_bet), int)
        self.sssertTrue(user_bet > 0)

    def test_act(self):
        """[summary]
        """
        user = User("test_user")
        sample_hand = [Card(Suit.DIAMONDS, 1)]
        user_action = user.act(sample_hand)
        self.assertTrue(user_action in Action)


class TestDealer(unittest.TestCase):

    def test_bet(self):
        """Dealer bet should be invalid
        """
        dealer = Dealer("test_dealer")
        self.assertRaises(NotImplementedError, dealer.bet())

    def test_act(self):
        """[summary]
        """
        dealer = Dealer("test_dealer")
        dealer_action = dealer.act()
        self.assertTrue(dealer_action in Action)


if __name__ == '__main__':
    unittest.main()
