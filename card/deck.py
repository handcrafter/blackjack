from .card import Card, Suit
import random


class Deck():
    """[summary]
    """

    def __init__(self):
        """[summary]
        """
        self.reset()

    def reset(self):
        """Refill the deck and keep it sorted
        """

        self.cards = []
        for suit in Suit:
            for number in range(1, 13):
                self.cards.append(Card(suit, number))

        self.sort()

    def sort(self):
        """sorts cards in the deck
        """

        self.cards.sort()

    def sort(self):
        raise NotImplementedError

    def draw(self) -> Card:
        """[summary]

        Returns:
            Card: [description]
        """

        return self.cards.pop()

    def shuffle(self):
        """[summary]
        """

        random.shuffle(self.cards)
