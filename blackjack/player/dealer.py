from typing import List

from blackjack.card import Card

from .player import Action, Player


class Dealer(Player):
    """[summary]
    """

    def __init__(self,
                 name: str):
        """[summary]

        Args:
            name (str): dealer name
        """
        super().__init__(name)

    def bet(self) -> int:
        """Dealer cannot bet

        Raises:
            NotImplementedError: Dealer should not bet

        Returns:
            int: invalid output
        """
        raise NotImplementedError("Dealer should not be betting")

    def act(self,
            hand: List[Card]) -> Action:
        """Dealer must be hitting when the hand is less than 16

        Args:
            hand (List[Card]): Implement Dealer's action when total value of card is less than16
        Returns:
            Action: Dealer hits when total value of card is less than 16
        """
        sum = 0
        for card in hand:
            sum += card.number

        action = Action.STAY
        if sum < 16:
            action = Action.HIT

        return action
