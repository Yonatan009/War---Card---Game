from Deck import Deck
from Player import Player
from Game import Game

player = Player("Nora", Deck(is_empty=True))
computer = Player("Computer", Deck(is_empty=True), is_computer=True)
deck = Deck()

game = Game(player, computer, deck)

game.print_welcome_message()

while not game.check_game_over():
    game.start_battle()
    game.print_stats()

    answer = input("\nAre you ready for the next round?\nPress Enter to continue. Enter X to stop.")

    if answer.lower() == "x":
        break
