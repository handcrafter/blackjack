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



        Returns:
            int: amount of money the player has bet
        """
        user_bet = 0
        while True:
            try:
                user_bet = int(input("How much do you want to bet?")
                break
            except ValueError:
                print("Wrong input. Try again")
        return user_bet



    def act(self) -> Action:
        """Ask the player to hit or stay

        Returns:
            Action: action taken by the player
        """
        player_action=0
        while True:
            user_action=input("type h for hit and s for stay")
            if user_action[0].lower() == 'h':
                print("Player hits")
                player_action=Action.HIT
            elif:
                user_action[0].lower() == 's':
                print("Player stays")
                player_action=Action.STAY
            else:
                print("Wrong input.Try again")
                continue
            break
        return player_action
