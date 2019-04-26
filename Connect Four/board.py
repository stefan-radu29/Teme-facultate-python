from texttable import Texttable
import unittest
from exception import BoardError
import copy

class Board:

    '''Class for representing the board of the game.'''

    def __init__(self):
        '''Constructor for the Board class. The board is represented as a 6x7 matrix.'''
        self._data = [7*[" "], 7*[" "], 7*[" "], 7*[" "], 7*[" "], 7*[" "]]

    def __str__(self):
        '''Overriding the str function so that we can return a string representing the board, for printing on the screen.'''
        display_board = Texttable()
        for row in range(0, 6):
            display_board.add_row(self._data[row])
        return display_board.draw()

    def move(self, column, symbol):
        '''
        Function for placing a disc on the board.
        :param column: the column on which the disc is placed.
        :param symbol: the symbol used for representing the human player(X) and the computer(O)
        :return:
        exception: raises BoardError if the column number exceeds the size of the board or if the column is full.
        '''
        if column > 6 or column < 0:
            raise BoardError("Column number must be between 1 and 7!")
        elif self._data[0][column] != " ":
            raise BoardError("Column full!")
        else:
            row = 5
            while self._data[row][column] != " ":
                row = row - 1
            self._data[row][column] = symbol

    def win(self):
        '''
        Function that checks whether or not the game played on a board has been won or not by one of the players.
        :return: True if one of the players won or False otherwise
        '''
        for row in range(0, 6):
            for column in range(0, 4):
                if self._data[row][column] != " " and self._data[row][column] == self._data[row][column+1] and self._data[row][column+1] == self._data[row][column+2] and self._data[row][column+2] == self._data[row][column+3]:
                    return True
        for column in range(0, 7):
            for row in range(0, 3):
                if self._data[row][column] != " " and self._data[row][column] == self._data[row+1][column] and self._data[row+1][column] == self._data[row+2][column] and self._data[row+2][column] == self._data[row+3][column]:
                    return True
        for row in range(3, 6):
            for column in range(0, 4):
                if self._data[row][column] != " " and self._data[row][column] == self._data[row-1][column+1] and self._data[row-1][column+1] == self._data[row-2][column+2] and self._data[row-2][column+2] == self._data[row-3][column+3]:
                    return True
        for row in range(0, 3):
            for column in range(0, 4):
                if self._data[row][column] != " " and self._data[row][column] == self._data[row+1][column+1] and self._data[row+1][column+1] == self._data[row+2][column+2] and self._data[row+2][column+2] == self._data[row+3][column+3]:
                    return True
        return False

    def tie(self):
        '''
        Function that checks whether or not the game played on a board has ended in  a tie.
        :return: True if the game is a tie or False otherwise.
        '''
        if self.win() == False:
            for column in range(0, 7):
                if self._data[0][column] == " ":
                    return False
            return True
        return False

    def copy(self):
        '''
        Function for copying the actual state of the board
        :return: a copy of the board
        '''
        board_copy = Board()
        board_copy._data = copy.deepcopy(self._data)
        return board_copy

    def get_possible_moves(self):
        '''
        Function that returns all the columns which are not full and on which there can be placed at least one more disc.
        :return: list containing columns which are not full
        '''
        possible_moves = []
        for column in range(0, 7):
            if self._data[0][column] == " ":
                possible_moves.append(column)
        return possible_moves

class Test_Board(unittest.TestCase):

    def setUp(self):
        self.board_win_horizontal = Board()
        for column in range(0, 4):
            self.board_win_horizontal.move(column, "O")

        self.board_win_vertical = Board()
        for i in range(0, 4):
            self.board_win_vertical.move(1, "O")

        self.board_win_diagonal = Board()
        for column in range(0, 3):
            self.board_win_diagonal.move(column, "O")
        for column in range(1, 3):
            self.board_win_diagonal.move(column, "O")
        self.board_win_diagonal.move(2, "O")
        self.board_win_diagonal.move(3, "X")
        for i in range(0, 3):
            self.board_win_diagonal.move(3, "O")

        self.board_full_first_column = Board()
        for i in range(0, 6):
            if i%2 == 0:
                self.board_full_first_column.move(0, "X")
            else:
                self.board_full_first_column.move(0, "O")

    def tearDown(self):
        self.board_full_first_column = None
        self.board_win_horizontal = None
        self.board_win_vertical = None
        self.board_win_diagonal = None
        self.board_tie = None

    def test_win(self):
        self.assertTrue(self.board_win_horizontal.win())
        self.assertTrue(self.board_win_vertical.win())
        self.assertTrue(self.board_win_diagonal.win())

    def test_get_possible_moves(self):
        options = self.board_full_first_column.get_possible_moves()
        self.assertEqual(options, [1, 2, 3, 4, 5, 6])
