from .player import Player


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
            hand (List[Card]): [description]

        Raises:
            NotImplementedError: [description]

        Returns:
            Action: [description]
        """
        raise NotImplementedError
