from service import Service
from exception import BoardError
class Game:

    def __init__(self, service):
        self._service = service

    def run(self):
        board = self._service.board
        player_move = True
        while board.win() is False and board.tie() is False:
            try:
                if player_move is True:
                    print(board)
                    print("Choose a column on which to place your disc.")
                    column = self._ui_read_move()
                    self._service.player_move(column)
                else:
                    self._service.computer_move()
                player_move = not player_move
            except BoardError as board_error:
                print(board_error)
        print(board)
        print("Game over!")
        if board.win() is True:
            if player_move is True:
                print("Computer won!")
            elif player_move is False:
                print("Player won!")
        elif board.tie() is True:
            print("Tie!")
        wait = input("Press a key to exit...")

    def _ui_read_move(self):
        while True:
            try:
                column = int(input())
                return column - 1
            except Exception:
                print("Invalid move. Input the number of the column on which you want to insert the disc( between 1 and 7).")





