class Player:
    def __init__(self, name):
        self.name = name
        self.cards = []

    def __str__(self):
        deck_comp = ""
        for card in self.cards:
            deck_comp += "\n" + card.__str__()
        return f"{self.name} deck:  + {deck_comp}"

    def get_card(self, card):
        self.cards.append(card)
