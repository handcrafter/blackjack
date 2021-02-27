from table import Table
from player import User, Dealer


def main():
    """Main function for blackjack application

    blackjack table and players are preapred
    game will be played until there is no player on the table
    """
    table = Table()

    player = User("player1")
    # table.add_player(player)

    print(f"There are {table.get_num_players()} players on the table")

    num_game = 0
    playing = True
    while playing:
        print(f"Starting game {num_game+1}")

        # table.play_game()

        if table.get_num_players() == 0:
            print(f"Every player has left the table")
            break

    print(f"Good bye")


if __name__ == "__main__":
    main()
