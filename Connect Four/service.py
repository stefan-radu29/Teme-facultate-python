from board import Board
import unittest
from random import choice

class Service:

    '''Class that contains the method needed for performing the services required by the problem.'''

    def __init__(self, board):
        '''
        Constructor for the Service class.
        :param board: an instance of the Board class, representing the board of the game
        '''
        self._board = board

    @property
    def board(self):
        '''
        Property representing the getter for the board.
        :return:
        '''
        return self._board

    def __str__(self):
        '''
        Overriding the str method.
        :return: the board represented as a string, for printing on the screen
        '''
        return str(self._board)

    def player_move(self, column):
        '''
        Function for adding a disc on the board on a position chosen by the human player.
        :param column: the column on which the player wishes to add a disc
        :return:
        '''
        self._board.move(column, "X")

    def computer_move(self):
        '''Function for implementing the computer player. It is going to move to win
        the game whenever possible and to block the human player’s attempts at 1-move victory,
        whenever possible. Otherwise, it chooses a random column from those which are not full and places a disc.'''
        possible_moves = self._board.get_possible_moves()

        '''Tries to win'''
        for move in possible_moves:
            board_copy = self._board.copy()
            board_copy.move(move, "O")
            if board_copy.win() == True:
                self._board.move(move, "O")
                return

        '''Blocks the player.'''
        for move in possible_moves:
            board_copy = self._board.copy()
            board_copy.move(move, "X")
            if board_copy.win() == True:
                self._board.move(move, "O")
                return

        self._board.move(choice(possible_moves), "O")

class Test_Service(unittest.TestCase):
    def setUp(self):
        self.board = Board()
        self.service = Service(self.board)

    def tearDown(self):
        self.board = None
        self.service = None

    def test_move_human_player(self):
        self.service.player_move(1)
        board = self.service.board
        self.assertEqual(board._data[5][1], "X")

    def test_computer_move(self):
        for j in range(0, 3):
            self.service.player_move(j)
        self.service.computer_move()
        board = self.service.board
        self.assertEqual(board._data[5][3], "O")
        board.move(4, "O")
        board.move(5, "O")
        self.service.computer_move()
        self.assertTrue(board.win())