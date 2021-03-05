import unittest

from blackjack.card import Card, Suit
from blackjack.player import Action, Dealer, User


class TestUser(unittest.TestCase):

    def test_bet(self):
        """testing if player puts valid input for betting
        """
        user = User("test_user")
        user_bet = user.bet()
        self.assertEqual(type(user_bet), int)
        self.assertTrue(user_bet > 0)

    def test_act(self):
        """testing if player puts valid input for action
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
        self.assertRaises(NotImplementedError, dealer.bet)

    def test_act(self):
        """testing if dealer keeps hitting 
           until total sum of cards reach 17.
        """
        dealer = Dealer("test_dealer")

        # total value is less than 16, expected to hit
        dealer_action = dealer.act([Card(Suit.DIAMONDS, 1)])
        self.assertTrue(dealer_action in Action)
        self.assertEqual(dealer_action, Action.HIT)

        # total value is greather than 16, expected to stay
        dealer_action_stay = dealer.act([Card(Suit.DIAMONDS, 10), Card(Suit.SPADES, 9)])  # action hit
        self.assertTrue(dealer_action_stay in Action)
        self.assertEqual(dealer_action_stay, Action.STAY)  # if () result is false, then pass/true


if __name__ == '__main__':
    unittest.main()
