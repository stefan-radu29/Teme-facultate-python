import unittest
from board import Board

class Controller:

    def __init__(self, board):
        self._board = board

    def show_board(self):
        return str(self._board)

    def start(self):
        self._board.starting_board()

    def cheat(self):
        return self._board.return_cheat_board()

    def warp(self, row, column):
        """
        Function that moves the ship to the new coordinate, which must be on the same rank,file or diagonal as the starting position.
        input: row, integer between 1 and 8
               column, integer between 1 and 8
        output: moves the ship to the new coordinate if possible, if there is an enemy ship at the new coordinate the ship is destroyed
        resulting in game over
        exception: an exception is raised if there is a star in the way of the ship and the ship is not moved
        """
        if column > 8 or column < 1:
            raise ValueError("invalid column!")
        row = row - 1
        column = column - 1
        self._board.move_ship(row, column)

    def fire(self,row, column):
        if column > 8 or column < 1:
            raise ValueError("invalid column!")
        ship_position = self._board.get_ship_position()
        row = row - 1
        column = column -1
        if row > ship_position[0] + 1 or column > ship_position[1] + 1 or row < ship_position[0] - 1 or column < ship_position[1] - 1:
            raise ValueError("Cannot fire that far!")
        enemies = self._board.get_enemies_around_ship()
        target = [row, column]
        if target in enemies:
            self._board.destroy_enemy(row, column)
        else:
            raise ValueError("No ship here!")

    def win(self):
        enemies = self._board.get_enemy_positions()
        if enemies == []:
            return True
        else:
            return False


class Test_warp(unittest.TestCase):
    def setUp(self):
        self._board = Board()
        self._controller = Controller(self._board)

    def tearDown(self):
        self._board = None
        self._controller = None

    def test_warp(self):
        self._board.starting_board()
        original_position = self._board.get_ship_position()
        self._controller.warp(original_position[0] + 2, original_position[1] + 2)
        self.assertEqual(self._board.get_ship_position(), [original_position[0] + 1, original_position[1] + 1])
