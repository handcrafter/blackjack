from .card import Card, Suit
import random


class Deck():
    """[summary]
    """

    def __init__(self):
        """[summary]
        """
        self.cards = []
        for i in suit:
            for j in number:
                self.cards.append(Card(suit, number))
     reset()

    def reset(self):
        """Refill the deck and keep it sorted
        """

        raise NotImplementedError

        new_deck = sort(self.cards)
        return new_deck

    def draw(self) -> Card:
        """[summary]

        Returns:
            Card: [description]
        """

        raise NotImplementedError

        draw_card = self.cards.pop()

        return draw_card

    def shuffle(self):
        """[summary]
        """

        raise NotImplementedError
        random.shuffle(self.cards)
