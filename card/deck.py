from .card import Card, Suit


class Deck():
    """[summary]
    """

    def __init__(self):
        """[summary]
        """
        self.cards = []
        self.cards.append(Card(Suit.DIAMONDS, 4))

    def draw(self) -> Card:
        """[summary]

        Returns:
            Card: [description]
        """

        raise NotImplementedError

    def shuffle(self):
        """[summary]
        """

        raise NotImplementedError
