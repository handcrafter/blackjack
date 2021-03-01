from .player import Player, Action


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

        user_bet = 0
        while True:
            try:
                user_bet = int(input("How much do you want to bet?"))
                if user_bet < 0:
                    raise ValueError
                break
            except ValueError:
                print("Wrong input. Try again")
        return user_bet

    def act(self,
            hand: List[Card]) -> Action:
        """Ask the user to hit or stay

        Returns:
            Action: action taken by the user
        """

        player_action = Action.STAY
        while True:
            user_action = input("type h for hit and s for stay")
            if user_action[0].lower() == 'h':
                print("Player hits")
                player_action = Action.HIT
            elif user_action[0].lower() == 's':
                print("Player stays")
                player_action = Action.STAY
            else:
                print("Wrong input.Try again")
                continue
            break
        return player_action
