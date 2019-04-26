from repository.grade_repository import Grade_repository
from domain.exceptions import RepositoryError
import pickle

class Grade_repository_pickle_file(Grade_repository):

    def __init__(self, file_name="grades.pickle"):
        Grade_repository.__init__(self)
        self.__file_name = file_name
        self.__load_from_file()

    def add(self, grade):
        Grade_repository.add(self, grade)
        self.__store_to_file()

    def remove(self, student_ID, assignment_ID):
        Grade_repository.remove(self, student_ID, assignment_ID)
        self.__store_to_file()

    def update(self, student_ID, assignment_ID, numeric_value_grade):
        Grade_repository.update(self, student_ID, assignment_ID, numeric_value_grade)
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