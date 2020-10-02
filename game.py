from deck import Deck
from player import Player


class Game:
    def __init__(self):
        self.deck = Deck()
        self.players = []

    def get_player_count(self):
        while True:
            try:
                self.player_count = int(input("Enter the no. of players: "))
                break
            except ValueError:
                print("I couldn't quite understand that.")

    def get_players_name(self):
        while True:
            for index in range(self.player_count):
                player_name = input(f"Enter player no {index + 1}'s name: ")
                self.players.append(Player(player_name))
            break

    def init(self):
        self.get_player_count()
        self.get_players_name()

    def distribute_cards(self):
        self.deck.shuffle()
        for player in self.players:
            for _ in range(3):
                player.cards.append(self.deck.deal_one())

    def trail(self, card_list):
        return card_list[0].rank == card_list[1].rank == card_list[2].rank

    def straight_flush(self, card_list):
        return self.color(card_list) and self.run(card_list)

    def run(self, card_list):
        card_values = [card.value for card in card_list]

        # Check if the values are consecutive or for [A,2,3]
        return sorted(card_values) == list(
            range(min(card_values), max(card_values) + 1)
        ) or sorted(card_values) in [2, 3, 14]

    def color(self, card_list):
        # Get suits of each card
        card_suits = [card.suit for card in card_list]
        return len(set(card_suits)) <= 1

    def pair(self, card_list):
        card_values = [card.value for card in card_list]

        if card_values[0] == card_values[1] and card_values[1] != card_values[2]:
            return True
        if card_values[1] == card_values[2] and card_values[1] != card_values[0]:
            return True
        if card_values[0] == card_values[2] and card_values[0] != card_values[1]:
            return True
        return False

    def start(self):
        self.init()
        self.distribute_cards()

        player_card_sequence = []

        # Check trail
        for player in self.players:
            if self.trail(player.cards):
                player_card_sequence.append("Trail")
            elif self.straight_flush(player.cards):
                player_card_sequence.append("Straight Flush")
            elif self.run(player.cards):
                player_card_sequence.append("Run")
            elif self.color(player.cards):
                player_card_sequence.append("Color")
            elif self.pair(player.cards):
                player_card_sequence.append("Pair")
            else:
                player_card_sequence.append("High Card")

        print(player_card_sequence)