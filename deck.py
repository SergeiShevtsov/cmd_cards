import random

from card import Card, Suits


class Deck:

    def __init__(self):
        self._cards = []

    def add(self, card: Card):
        self._cards.append(card)

    def pop(self): #take card from top
        if len(self._cards) == 0:
            return None
        return self._cards.pop()

    @property
    def size(self):
        return len(self._cards)

    @property
    def empty(self):
        return len(self._cards) == 0

    def shuffle(self): #перетасовать колоду
        for i in range(4):
            random.shuffle(self._cards)

    def __str__(self):
        return f"Колода в которой {self.size} карт"


def deck_36_cards():
    deck = Deck()
    for value in [6,7,8,9,10,'J','Q','K','A']:
        for suit in list(Suits):
            deck.add(Card(value, suit))
    return deck