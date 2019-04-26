from repository.assignment_repository import Assignment_repository
from domain.exceptions import RepositoryError
import pickle

class Assignment_repository_pickle_file(Assignment_repository):
    def __init__(self, file_name="assignments.pickle"):
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
        file = open(self.__file_name, "rb")
        try:
            self._data = pickle.load(file)
        except EOFError:
            self._data = []
        except Exception as exception:
            raise RepositoryError(str(exception))
        finally:
            file.close()

    def __store_to_file(self):
        file = open(self.__file_name, "wb")
        pickle.dump(self._data, file)
        file.close()