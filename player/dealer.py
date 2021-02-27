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
