import unittest

from blackjack.card import Card, Deck, Suit


class TestCard(unittest.TestCase):

    def test_card(self):
        """make sure the suit and number provided to the card is valid

        """
        card = Card(Suit.DIAMONDS, 2)
        self.assertEqual(card.suit, Suit.DIAMONDS)
        self.assertEqual(card.number, 2)

    def test_lt(self):
        """using two cards, make sure lt operation retuns valid output

        """
        card1 = Card(Suit.DIAMONDS, 2)
        card2 = Card(Suit.SPADES, 5)
        card3 = Card(Suit.HEARTS, 13)

        self.assertTrue(card1 < card2)
        self.assertFalse(card2 < card3)
        self.assertFalse(card3 < card1)

# class TestDeck(unittest.TestCase):

#     def test_reset(self):
#         raise NotImplementedError

#     def test_sort(self):
#         raise NotImplementedError

#     def test_shuffle(self):
#         """Check if shuffle is valid by checking first, last card, and the number of cards in the deck
#         """
#         deck = Deck()
#         original_first_card = deck.cards[0]
#         original_last_card = deck.cards[-1]
#         original_card_length = len(deck.cards)

#         deck.shuffle()

#         shuffled_first_card = deck.cards[0]
#         shuffled_last_card = deck.cards[1]
#         shuffled_card_length = len(deck.cards)

#         is_first_card_diff = (original_first_card.number != shuffled_first_card.number) or (
#             original_first_card.suit != shuffled_first_card.suit)
#         is_last_card_diff = (original_last_card.number != shuffled_last_card.number) or (
#             original_last_card.suit != shuffled_last_card.suit)

#         self.assertFalse(is_first_card_diff and is_last_card_diff)
#         self.assertEqual(original_card_length, shuffled_card_length)

#     def test_draw(self):
#         """When card is drawn the number cards in the deck must change and the drawn card must be valid
#         """
#         deck = Deck()
#         before_draw_card_length = len(deck.cards)

#         card_drawn = deck.draw()

#         after_draw_card_length = len(deck.cards)

#         self.assertEqual(after_draw_card_length, before_draw_card_length + 1)
#         self.assertTrue(card_drawn.number < 14 and card_drawn.number > 0)
#         self.assertEqual(card_drawn.suit in Suit)


if __name__ == '__main__':
    unittest.main()
