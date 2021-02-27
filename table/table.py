from card import Deck, Card
from player import Dealer, Player
from typing import List


class Table():
    """BlackJack table

    players can join and play blackjack game
    """

    def __init__(self):
        """initialize Table class
        """
        self.players = []
        self.deck = Deck()
        self.dealer = Dealer("dealer")

    def get_num_players(self) -> int:
        """get number of players on the table

        Returns:
            int: number of players on the table
        """
        return len(self.players)

    def add_player(self,
                   player: Player):
        """add a player

        Args:
            player (Player): player who is willing to join the game
        """
        self.players.append(player)

    def is_busted(self, card: List[Card]) -> bool:
        """[summary]

        Args:
            card (List[Card]): [description]

        Returns:
            bool: true if the set of cards lead to busted case
        """

    def play_game(self) -> bool:
        """play single game of blackjack

        Returns:
            bool: true if every player left the game during the game
        """

        if self.get_num_players() == 0:
            raise ValueError(f"There is no player on the table")

        # TODO::shuffle deck

        # TODO::ask each player how much they are willing to bet

        # TODO::deal initial cards to dealer

        # TODO::deal initial cards to player

        # while user card is still valid
            # TODO::ask each player to pick an action
            # TODO::deal extra card if necessary

        # TODO::deal final cards to dealer

        # TODO::check the results

        # TODO::update player/dealer stats and the money

        return self.get_num_players() == 0
