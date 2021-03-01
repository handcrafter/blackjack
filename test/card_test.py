from card import Deck, Card, Suit

import unittest


class TestCard(unittest.TestCase):

    def test_card(self):
        card = Card(Suit.DIAMONDS, 2)
        self.assertEqual(card.suit, Suit.DIAMONDS)
        self.assertEqual(card.number, 2)


class TestDeck(unittest.TestCase):

    def __init__(self):
        self.deck = Deck()

    def test_reset(self):
        raise NotImplementedError

    def test_sort(self):
        raise NotImplementedError

    def test_shuffle(self):
        original_first_card = self.cards[0]
        original_last_card = self.cards[-1]
        original_card_length = len(self.cards)

        self.deck.shuffle()

        shuffled_first_card = self.cards[0]
        shuffled_last_card = self.cards[1]
        shuffled_card_length = len(self.cards)

        is_first_card_diff = (original_first_card.number != shuffled_first_card.number) or (
            original_first_card.suit != shuffled_first_card.suit)
        is_last_card_diff = (original_last_card.number != shuffled_last_card.number) or (
            original_last_card.suit != shuffled_last_card.suit)

        self.assertFalse(is_first_card_diff and is_last_card_diff)
        self.assertEqual(original_card_length, shuffled_card_length)

    def test_draw(self):
        before_draw_card_length = len(self.cards)

        card_drawn = self.deck.draw()

        after_draw_card_length = len(self.cards)

        self.assertEqual(after_draw_card_length, before_draw_card_length + 1)
        self.assertEqual(card_drawn.number < 14 and card_drawn.number > 0)
        self.assertEqual(card_drawn.suit in Suit)


if __name__ == '__main__':
    unittest.main()
