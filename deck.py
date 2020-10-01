from base import SUITS, RANKS
from card import Card
import random


class Deck:
    def __init__(self):
        self.deck = []

        for suit in SUITS:
            for rank in RANKS:
                self.deck.append(Card(suit, rank))

    def __str__(self):
        deck_comp = ""
        for card in self.deck:
            deck_comp += "\n" + card.__str__()
        return "Your deck: " + deck_comp

    def shuffle(self):
        random.shuffle(self.deck)

    def deal_one(self):
        return self.deck.pop()