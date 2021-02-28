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
        """Ask the user to bet

        Raises:
            NotImplementedError: [description]

        Returns:
            int: amount of money the player has bet
        """
        while True:
            try:
                inp_bet = input("How much do you want to bet?")
            except ValueError:
                print("Wrong input. Try again")
            else:
                break

        raise NotImplementedError

    def act(self) -> Action:
        """Ask the player to hit or stay

        Returns:
            Action: action taken by the player
        """
        while True:
            inp_action = input("type h for hit and s for stay")
            if inp_action[0].lower() == 'h':
                print("Player hits")
                return Action.HIT
            elif:
                inp_action[0].lower() == 's':
                print("Player stands")
                return Action.STAY
            else:
                print("Wrong input.Try again")
                continue
            break

        raise NotImplementedError
