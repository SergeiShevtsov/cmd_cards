from player import Player
from blackjack import BlackJack

game = BlackJack()
game.add_player(Player("Petya"))
game.add_player(Player("Vova"))

game.play()