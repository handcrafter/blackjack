from .card import Card, Suit


class Deck():
    """[summary]
    """

    def __init__(self):
        """[summary]
        """
        self.cards = []
        # reset()

    def reset(self):
        """Refill the deck and keep it sorted
        """

        raise NotImplementedError

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
