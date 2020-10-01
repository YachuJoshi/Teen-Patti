from deck import Deck
from player import Player

deck = Deck()
players = []
player_count = int(input("Enter the no. of players: "))

while True:

    for index, item in enumerate(list(range(player_count))):
        player_name = input(f"Enter player no{index + 1}'s name: '")
        players.append(Player(player_name))
