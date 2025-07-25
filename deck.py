class Deck:
    def __init__(self):
        self.cards = []

    def add_card(self, card):
        self.cards.append(card)

    def shuffle(self):
        import random
        random.shuffle(self.cards)

    def deal(self):
        return self.cards.pop() if self.cards else None