from texttable import Texttable
import random

class Board:

    def __init__(self):
        self._data = [8*[" "],8*[" "],8*[" "],8*[" "],8*[" "],8*[" "],8*[" "],8*[" "]]
        self._enemy_ships = []
        self._placed_ship_coordinates = None

    def starting_board(self):
        placed_stars = 0
        while placed_stars < 10:
            row = random.randrange(0,7)
            column = random.randrange(0,7)
            if row == 0 and column == 0:
                if self._data[row][column]==self._data[row][column+1]==self._data[row+1][column]==self._data[row+1][column+1]==" ":
                    self._data[row][column] = "*"
                    placed_stars += 1
            elif row == 0 and column == 7:
                if self._data[row][column]==self._data[row][column-1]==self._data[row+1][column]==self._data[row+1][column-1]==" ":
                    self._data[row][column] = "*"
                    placed_stars += 1
            elif row == 7 and column == 0:
                if self._data[row][column]==self._data[row][column+1]==self._data[row-1][column]==self._data[row-1][column+1]==" ":
                    self._data[row][column] = "*"
                    placed_stars += 1
            elif row == 7 and column == 7:
                if self._data[row][column]==self._data[row][column-1]==self._data[row-1][column]==self._data[row-1][column-1]==" ":
                    self._data[row][column] = "*"
                    placed_stars += 1
            elif column == 0:
                if self._data[row][column] == self._data[row-1][column] == self._data[row+1][column] == self._data[row - 1][column + 1] == self._data[row][column + 1]==self._data[row+1][column+1] == " ":
                    self._data[row][column] = "*"
                    placed_stars += 1
            elif column == 7:
                if self._data[row][column] == self._data[row-1][column] == self._data[row+1][column] == self._data[row - 1][column - 1] == self._data[row][column - 1]==self._data[row+1][column-1] == " ":
                    self._data[row][column] = "*"
                    placed_stars += 1
            elif row == 0:
                if self._data[row][column] == self._data[row+1][column] == self._data[row+1][column-1] == self._data[row + 1][column + 1] == self._data[row][column - 1]==self._data[row][column+1] == " ":
                    self._data[row][column] = "*"
                    placed_stars += 1
            elif row == 7:
                if self._data[row][column] == self._data[row-1][column] == self._data[row-1][column-1] == self._data[row - 1][column + 1] == self._data[row][column - 1]==self._data[row][column+1] == " ":
                    self._data[row][column] = "*"
                    placed_stars += 1
            else:
                if self._data[row -1][column-1] == self._data[row-1][column] == self._data[row-1][column + 1] ==self._data[row][column -1] ==self._data[row][column] ==self._data[row][column + 1] ==self._data[row+1][column-1] ==self._data[row+1][column] ==self._data[row+1][column+1] == " ":
                    self._data[row][column] = "*"
                    placed_stars += 1

        placed_ship = False
        while placed_ship == False:
            row = random.randrange(0, 7)
            column = random.randrange(0, 7)
            if self._data[row][column] == " ":
                self._data[row][column] = "E"
                placed_ship = True
                self._placed_ship_coordinates = [row, column]

        placed_enemy_ships = 0
        while placed_enemy_ships != 3:
            row = random.randrange(0, 7)
            column = random.randrange(0, 7)
            if self._data[row][column] == " " and [row,column] not in self._enemy_ships:
                self._enemy_ships.append([row, column])
                placed_enemy_ships += 1

    def return_cheat_board(self):
        display_board = Texttable()
        display_board.header(["0", "1", "2", "3", "4", "5", "6", "7", "8"])
        for enemy in self._enemy_ships:
            self._data[enemy[0]][enemy[1]] = "B"
        row = 0
        for letter in ["A", "B", "C", "D", "E", "F", "G", "H"]:
            list_to_add = self._data[row]
            new_row = [letter]
            new_row.extend(list_to_add)
            display_board.add_row(new_row)
            row += 1
        drawn_board = display_board.draw()
        return drawn_board

    def __str__(self):
        display_board = Texttable()
        display_board.header(["0","1","2","3","4","5","6","7","8"])
        enemies = self.get_enemies_around_ship()
        for enemy in enemies:
            self._data[enemy[0]][enemy[1]] = "B"
        row = 0
        for letter in ["A","B","C","D","E","F","G","H"]:
            list_to_add = self._data[row]
            new_row = [letter]
            new_row.extend(list_to_add)
            display_board.add_row(new_row)
            row += 1
        drawn_board = display_board.draw()
        return drawn_board

    def get_enemy_positions(self):
        return self._enemy_ships[:]

    def get_enemies_around_ship(self):
        show_enemies = []
        row = self._placed_ship_coordinates[0]
        column = self._placed_ship_coordinates[1]
        if [row-1,column-1] in self._enemy_ships:
            show_enemies.append([row-1,column-1])
        if [row-1,column] in self._enemy_ships:
            show_enemies.append([row-1,column])
        if [row-1,column+1] in self._enemy_ships:
            show_enemies.append([row-1,column+1])
        if [row,column-1] in self._enemy_ships:
            show_enemies.append([row,column-1])
        if [row,column] in self._enemy_ships:
            show_enemies.append([row,column])
        if [row,column+1] in self._enemy_ships:
            show_enemies.append([row,column+1])
        if [row+1,column-1] in self._enemy_ships:
            show_enemies.append([row+1,column-1])
        if [row+1,column] in self._enemy_ships:
            show_enemies.append([row+1,column])
        if [row+1,column+1] in self._enemy_ships:
            show_enemies.append([row+1,column+1])
        return show_enemies

    def get_ship_position(self):
        return self._placed_ship_coordinates[:]

    def destroy_enemy(self,row,column):
        self._data[row][column] = " "
        self._enemy_ships.remove([row, column])

    def move_ship(self, row, column):
        """
        Function for moving a ship to a new position
        :param row: integer, row on which the ship will be moved
        :param column: integer, column on which the ship will be moved
        :return: the ship is moved on a new position
        """
        if row == self._placed_ship_coordinates[0]:
            self._data[self._placed_ship_coordinates[0]][self._placed_ship_coordinates[1]] = " "
            self._data[row][column] = "E"
            self._placed_ship_coordinates = [row, column]
            return
        elif column == self._placed_ship_coordinates[1]:
            self._data[self._placed_ship_coordinates[0]][self._placed_ship_coordinates[1]] = " "
            self._data[row][column] = "E"
            self._placed_ship_coordinates = [row, column]
            return
        for i in range(0, 7):
            if (row == self._placed_ship_coordinates[0] + i and column == self._placed_ship_coordinates[1] + i) or (row == self._placed_ship_coordinates[0] + i and column == self._placed_ship_coordinates[1] - i) or (row == self._placed_ship_coordinates[0] - i and column == self._placed_ship_coordinates[1] + i) or (row == self._placed_ship_coordinates[0] - i and column == self._placed_ship_coordinates[1] - i):
                self._data[self._placed_ship_coordinates[0]][self._placed_ship_coordinates[1]] = " "
                self._data[row][column] = "E"
                self._placed_ship_coordinates = [row, column]
                return
        raise ValueError("Invalid destination!")