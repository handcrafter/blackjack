from .player import Player


class User(Player):
    """[summary]

    """

    def __init__(self,
                 name: str):
        """[summary]

        Args:
            name (str): user name
        """
        super().__init__(name)
