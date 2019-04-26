from repository.assignment_repository import Assignment_repository
from domain.exceptions import RepositoryError
from domain.assignment import Assignment
from datetime import *

class Assignment_repository_text_file(Assignment_repository):
    def __init__(self, file_name="assignments.txt"):
        Assignment_repository.__init__(self)
        self.__file_name = file_name
        self.__load_from_file()

    def add(self, assignment):
        Assignment_repository.add(self, assignment)
        self.__store_to_file()

    def update(self, assignment_update):
        Assignment_repository.update(self, assignment_update)
        self.__store_to_file()

    def remove(self, ID):
        Assignment_repository.remove(self, ID)
        self.__store_to_file()

    def __load_from_file(self):
        try:
            file = open(self.__file_name, "r")
            line = file.readline().strip()
            while line != "":
                attributes = line.split(";")
                assignment = Assignment(int(attributes[0]), attributes[1], date(int(attributes[2]), int(attributes[3]), int(attributes[4])))
                Assignment_repository.add(self, assignment)
                line = file.readline().strip()
        except IOError as ioerror:
            raise RepositoryError(str(ioerror))
        finally:
            file.close()

    def __store_to_file(self):
        file = open(self.__file_name, "w")
        assignments = Assignment_repository.get_all(self)
        for assignment in assignments:
            store_to_file = str(assignment.ID) + ";" + assignment.description + ";" + str(assignment.deadline.year) + ";" + str(assignment.deadline.month) +";" + str(assignment.deadline.day) + "\n"
            file.write(store_to_file)
        file.close()
