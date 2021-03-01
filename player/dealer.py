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
        raise NotImplementedError

    def act(self,
            hand: List[Card]) -> Action:
        raise NotImplementedError
