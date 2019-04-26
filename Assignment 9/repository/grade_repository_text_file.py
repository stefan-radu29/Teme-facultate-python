from repository.grade_repository import Grade_repository
from domain.exceptions import RepositoryError
from domain.grade import Grade

class Grade_repository_text_file(Grade_repository):

    def __init__(self, file_name="grades.txt"):
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
        try:
            file = open(self.__file_name, "r")
            line = file.readline().strip()
            while line != "":
                attributes = line.split(";")
                if attributes[2] != "None":
                    grade = Grade(int(attributes[0]), int(attributes[1]), int(attributes[2]))
                else:
                    grade = Grade(int(attributes[0]), int(attributes[1]))
                Grade_repository.add(self, grade)
                line = file.readline().strip()
        except IOError as ioerror:
            raise RepositoryError(str(ioerror))
        finally:
            file.close()

    def __store_to_file(self):
        file = open(self.__file_name, "w")
        grades = Grade_repository.get_all(self)
        for grade in grades:
            store_to_file = str(grade.assignment_ID) + ";" + str(grade.student_ID) + ";" + str(grade.numeric_value) + "\n"
            file.write(store_to_file)
        file.close()


