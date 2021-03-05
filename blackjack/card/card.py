from enum import Enum


class Suit(Enum):

    DIAMONDS = 1
    CLUBS = 2
    HEARTS = 3
    SPADES = 4


class Card():
    """Card has two properties: suit and number, which are used to sort the cards.
    """

    def __init__(self,
                 suit: Suit,
                 number: int):
        """Card has a suit and a number, classifed as Suit and integerm, respectively.

        Args:
            suit (Suit): A suit is a suit/shape on card, classified as an Enum.
            number (int): A number is a number on card, classified as an integer.
        """
        self.suit = suit
        self.number = number

    def __lt__(self, other) -> bool:
        """Test if self and other card can be sorted based on their suit and number.

        Args:
            other ([bool]): self and other both refer to unique cards. 

        Returns:
            [bool]: We're using the two statements below as conditions to be applied to the sample cards under test_lt function in card.py (test).
                    Compare the cards.
        """

        # diamond = 1, club = 2, hearts = 3, spade = 4 added suit to __lt__ funciton.
        return self.suit.value < other.suit.value and self.number < other.number
