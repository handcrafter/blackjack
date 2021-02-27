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

    def bet(self) -> int:
        """Ask the user to bet

        Raises:
            NotImplementedError: [description]

        Returns:
            int: amount of money the user has bet
        """

        # TODO:: ask user using input()
        raise NotImplementedError

    def act(self) -> Action:
        """Ask the user to hit or stay

        Returns:
            Action: action taken by the user
        """

        # TODO:: ask user using input()
        raise NotImplementedError
