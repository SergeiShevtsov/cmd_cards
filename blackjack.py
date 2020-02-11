import re

from deck import Deck, deck_36_cards
from player import Player

# 36 карт
# ходят по очереди
# не вскрываемся 

class BlackJack:
    _deck = deck_36_cards()
    _players: [Player]
    _value_to_points = {
        6: 6,  
        7: 7,  
        8: 8,  
        9: 9,  
        10: 10, 
        'J': 2,
        'Q': 3,
        'K': 4,
        'A': 1,
    }

    def __init__(self):
        self._deck = deck_36_cards()
        self._deck.shuffle()
        self._players = []

    def add_player(self, player):
        self._players.append(player)

    def _count_players_score(self, player: Player):
        points_total = 0
        for card in player.cards:
            value = card.value # 6 - 10, "J" ...
            points = self._value_to_points[value]
            points_total += points
        return points_total

    def _get_yes_or_no(self):
        no_regexp = " *[нН][еЕ]?[тТ]?"
        yes_regexp = " *[дД][аА]?"

        take_card = None
        while take_card is None: 
            answer = input("Берешь карту? <Да/Нет>")
            if re.match(no_regexp, answer):
                take_card = False
            elif re.match(yes_regexp, answer):
                take_card = True
            else:
                print("Неправильный ответ, повторите")
        return take_card

    def play(self):
        # раздаем по 2 карты в начале игры
        for player in self._players:
            player.cards.append(self._deck.pop())
            player.cards.append(self._deck.pop())

        # игроки берут карты
        for player in self._players:
            self._player_turn(player)

        # определяем победителя
        best = 0, []
        for player in self._players:
            player_score = self._count_players_score(player)
            if player_score > 21: 
                player_score = 0
            if player_score == best[0]:
                best[1].append(player)
            elif player_score > best[0]:
                best = player_score, [player]

        print(f"Победители (набрали {best[0]} очков)")
        for winner in best[1]:
            print(player.name)

    def _player_turn(self, player: Player):
        print(f"Привет, {player.name}. Ходи.")
        
        while self._count_players_score(player) < 21:
            print(f"Очков: {self._count_players_score(player)}")
            take_card = self._get_yes_or_no()
            if take_card:
                card_from_deck = self._deck.pop()
                player.cards.append(card_from_deck)
                print(card_from_deck)
            else:
                break

        print(f"Хорошая игра, {player.name}. Ваш счет {self._count_players_score(player)}")

                
                
                


