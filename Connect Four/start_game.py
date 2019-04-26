from service import Service
from ui import Game
from board import Board

board = Board()
service = Service(board)
game = Game(service)
game.run()
