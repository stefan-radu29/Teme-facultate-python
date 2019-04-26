from board import Board
from controller import Controller
from ui import Game

board = Board()
controller = Controller(board)
game = Game(controller)
game.run()