from enum import Enum


class Suit(Enum):
    DIAMONDS = 1
    CLUBS = 2
    HEARTS = 3
    SPADES = 4


class Card():
    """[summary]
    """

    def __init__(self,
                 suit: Suit,
                 number: int):
        """[summary]

        Args:
            suit (Suit): [description]
            number (int): [description]
        """
        self.suit = suit
        self.number = number

    def __lt__(self, other):
        """[summary]

        Args:
            other ([type]): [description]

        Returns:
            [type]: [description]
        """

        # TODO:: use suit information
        return self.number < other.number
