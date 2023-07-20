from battleship import *
import random


def play_battleship(start_game):
    """a main function where the player and computer iterate in guessing the opponent's ship location"""
    # welcome message
    print("Ahoy Captain! Let's create your fleet!")

    # initial score for both players
    user_score = 0
    computer_score = 0

    # create fleet for the player
    player_fleet = create_player_fleet()
    print("Your fleet is ready!")
    create_map(player_fleet)  # create map after all ships are placed
    print("Your fleet: ", player_fleet)

    # fleet is created for pc
    computer_fleet = create_computer_fleet()
    print("Enemy's fleet is ready: ", computer_fleet)  # just checking if it works, delete before sending!

    # iteration of moves in guessing the opponent's ship location
    print("Let's destroy some enemy ships!")

    players_moves(computer_fleet, player_fleet)