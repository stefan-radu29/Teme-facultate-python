from repository.student_repository import Student_repository
from domain.exceptions import RepositoryError
import pickle

class Student_repository_pickle_file(Student_repository):

    def __init__(self, file_name="students.pickle"):
        Student_repository.__init__(self)
        self.__file_name = file_name
        self.__load_from_file()

    def add(self, student):
        Student_repository.add(self, student)
        self.__store_to_file()

    def update(self, student_update):
        Student_repository.update(self, student_update)
        self.__store_to_file()

    def remove(self, ID):
        Student_repository.remove(self, ID)
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