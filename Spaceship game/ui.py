class Game:

    def __init__(self, controller):
        self._controller = controller

    def run(self):
        self._controller.start()
        while self._controller.win() == False:
            try:
                print(self._controller.show_board())
                command = input().split(" ")
                if command[0] == "exit":
                    return
                elif command[0] == "cheat" and len(command) == 1:
                    self._ui_print_cheat()
                elif command[0] == "fire" and len(command) == 2:
                    self._ui_fire(command)
                elif command[0] == "warp" and len(command) == 2:
                    self._ui_warp(command)
                else:
                    raise ValueError("invalid command!")
            except ValueError as ve:
                print(ve)
            except TypeError as te:
                print(te)
        if self._controller.win() == True:
            print("You won!")

    def _ui_print_cheat(self):
        self._controller.cheat()

    def _ui_fire(self, command):
        coordinate = command[1]
        dict_of_letters = {"A":1,"B":2,"C":3,"D":4,"E":5,"F":6,"G":7,"H":8}
        if coordinate == "":
            raise ValueError("invalid command!")
        if coordinate[0] in dict_of_letters:
            row = dict_of_letters[coordinate[0]]
        else:
            raise ValueError("invalid row!")
        column = int(coordinate[1])
        self._controller.fire(row,column)

    def _ui_warp(self, command):
        coordinate = command[1]
        dict_of_letters = {"A": 1, "B": 2, "C": 3, "D": 4, "E": 5, "F": 6, "G": 7, "H": 8}
        if coordinate == "":
            raise ValueError("invalid command!")
        if coordinate[0] in dict_of_letters:
            row = dict_of_letters[coordinate[0]]
        else:
            raise ValueError("invalid row!")
        column = int(coordinate[1])
        self._controller.warp(row, column)

