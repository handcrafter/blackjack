from abc import ABC, abstractmethod
from enum import Enum
from typing import List

from blackjack.card import Card


class Action(Enum):
    HIT = 1
    STAY = 2


class Player(ABC):
    """[summary]
    """

    def __init__(self,
                 name: str):
        """[summary]

        Args:
            name (str): player name
        """
        self.name = name

    @abstractmethod
    def bet(self) -> int:
        """abstract method for getting the bet made by the player

        Returns:
            int: amount of money the player has bet
        """
        pass

    @abstractmethod
    def act(self,
            hand: List[Card]) -> Action:
        """abstract method for getting the action played by the player for the given hand

        Args:
            hand (List[Card]): hand of the user

        Returns:
            Action: action played by the user
        """
        pass
