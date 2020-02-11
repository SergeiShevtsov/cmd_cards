from enum import Enum

Suits = Enum("Suits", "Diamonds Hearts Spades Clubs")

_suit_to_picture = {
    Suits.Diamonds: "♦",
    Suits.Hearts  : "♥",
    Suits.Spades  : "♠",
    Suits.Clubs   : "♣"
}

class Card:

    def __init__(self, value, suit):
        value_ok = (isinstance(value, int) and (6 <= value <= 10) 
                 or isinstance(value, str) and (value in "JQKA"))
        suit_ok = suit in list(Suits)
        if not (value_ok and suit_ok):
            raise TypeError("Карта создана с неправильным значением либо мастью")
        self._value = value
        self._suit = suit

    @property
    def value(self):
        return self._value

    @property
    def suit(self):
        return self._suit

    def __str__(self):
        suit_symbol = _suit_to_picture[self._suit]
        return f"{self._value}{suit_symbol}"
