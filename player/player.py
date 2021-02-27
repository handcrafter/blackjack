from enum import Enum


class Action(Enum):
    HIT = 1
    STAY = 2


class Player():
    """[summary]
    """

    def __init__(self,
                 name: str):
        """[summary]

        Args:
            name (str): player name
        """
        self.name = name

    def bet(self) -> int:
        """Ask User to bet

        Raises:
            NotImplementedError: [description]

        Returns:
            int: amount of money the player has bet
        """
        raise NotImplementedError

    def act(self) -> Action:
        """Ask the player to hit or stay

        Returns:
            Action: action taken by the player
        """
        raise NotImplementedError
