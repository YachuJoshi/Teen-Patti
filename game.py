from deck import Deck
from player import Player
from functools import reduce
from time import sleep


class Game:
    def __init__(self):
        self.deck = Deck()
        self.players = []

    # Get player count >= 2
    def get_player_count(self):
        while True:
            try:
                self.player_count = int(input("Enter the no. of players: "))

                if self.player_count <= 1:
                    print("Cannot start game with 1 or less players")
                else:
                    break
            except ValueError:
                print("I couldn't quite understand that.")

    # Get player names
    def get_players_name(self):
        while True:
            for index in range(self.player_count):
                player_name = input(f"Enter player no {index + 1}'s name: ")
                self.players.append(Player(player_name))
            break

    # Print welcome messages and initialise game
    def init(self):
        print("WELCOME TO TEENPATTI! ")
        print("\nWINNER SEQUENCE: ")
        print(
            """
1. Trails
2. Pure Sequence or Straight Flush
3. Sequence or Run
4. Color
5. Pair
6. High Card
        """
        )
        self.get_player_count()
        self.get_players_name()

    # Deal 3 cards to each players
    def distribute_cards(self):
        for player in self.players:
            for _ in range(3):
                player.cards.append(self.deck.deal_one())

    # True if all ranks are same
    def trail(self, card_list):
        return card_list[0].rank == card_list[1].rank == card_list[2].rank

    # True if one has both run and color
    def straight_flush(self, card_list):
        return self.color(card_list) and self.run(card_list)

    # True if all ranks are consecutive
    def run(self, card_list):
        card_values = [card.value for card in card_list]

        # Check if the values are consecutive or for [A,2,3]
        return sorted(card_values) == list(
            range(min(card_values), max(card_values) + 1)
        ) or sorted(card_values) in [2, 3, 14]

    # True if all suits are same
    def color(self, card_list):
        # Get suits of each card
        card_suits = [card.suit for card in card_list]
        return len(set(card_suits)) <= 1

    # True if 2 ranks are same and one is different
    def pair(self, card_list):
        card_values = [card.value for card in card_list]

        if card_values[0] == card_values[1] and card_values[1] != card_values[2]:
            return True
        if card_values[1] == card_values[2] and card_values[1] != card_values[0]:
            return True
        if card_values[0] == card_values[2] and card_values[0] != card_values[1]:
            return True
        return False

    # Push player w/ their corresponding player ranks
    def push_player_rank_to(self, array, player, card_rank):
        card_values = [card.value for card in player.cards]
        array.append(
            {
                "name": player.name,
                "player_card": list(map((lambda card: card.__str__()), player.cards)),
                "card_rank": card_rank,
                "sum": reduce(
                    (lambda value_A, value_B: value_A + value_B), card_values
                ),
            }
        )

    # Start game
    def start(self):
        self.init()
        print("\nShuffling Deck....\n")
        sleep(2.4)
        self.deck.shuffle()
        self.distribute_cards()

        # Show player cards
        for player in self.players:
            print(player)
            sleep(1)

        players_with_trail = []
        players_with_pure_sequence = []
        players_with_run = []
        players_with_color = []
        players_with_pair = []
        players_with_high_card = []

        winner = None

        # Check Card Ranks for each player and assign a rank
        for player in self.players:
            if self.trail(player.cards):
                self.push_player_rank_to(players_with_trail, player, "Trails")
            elif self.straight_flush(player.cards):
                self.push_player_rank_to(
                    players_with_pure_sequence, player, "Pure Sequence"
                )
            elif self.run(player.cards):
                self.push_player_rank_to(players_with_run, player, "Run")
            elif self.color(player.cards):
                self.push_player_rank_to(players_with_color, player, "Color")
            elif self.pair(player.cards):
                self.push_player_rank_to(players_with_pair, player, "Pair")
            else:
                self.push_player_rank_to(players_with_high_card, player, "High Card")

        # Check for trails
        if players_with_trail:
            trails_sum = [player["sum"] for player in players_with_trail]
            winner_sum = max(trails_sum)

            for player in players_with_trail:
                if winner_sum == player["sum"]:
                    winner = player
                    break

        # Check for pure sequence
        elif players_with_pure_sequence:
            straight_flush_sum = [
                player["sum"] for player in players_with_pure_sequence
            ]
            winner_sum = max(straight_flush_sum)

            for player in players_with_pure_sequence:
                if winner_sum == player["sum"]:
                    winner = player
                    break

        # Check for run
        elif players_with_run:
            run_sum = [player["sum"] for player in players_with_run]
            winner_sum = max(run_sum)

            for player in players_with_run:
                if winner_sum == player["sum"]:
                    winner = player
                    break

        # Check for color
        elif players_with_color:
            color_sum = [player["sum"] for player in players_with_color]
            winner_sum = max(color_sum)

            for player in players_with_color:
                if winner_sum == player["sum"]:
                    winner = player
                    break

        # Check for pair
        elif players_with_pair:
            pair_sum = [player["sum"] for player in players_with_pair]
            winner_sum = max(pair_sum)

            for player in players_with_pair:
                if winner_sum == player["sum"]:
                    winner = player
                    break

        # Check for high card
        elif players_with_high_card:
            high_card_sum = [player["sum"] for player in players_with_high_card]
            winner_sum = max(high_card_sum)

            for player in players_with_high_card:
                if winner_sum == player["sum"]:
                    winner = player
                    break

        else:
            pass

        print(
            f"""
Winner: {winner["name"]}
Card: {winner["player_card"]}
Rank: {winner["card_rank"]}
"""
        )
