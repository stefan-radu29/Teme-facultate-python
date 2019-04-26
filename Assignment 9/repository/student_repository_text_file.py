from repository.student_repository import Student_repository
from domain.exceptions import RepositoryError
from domain.student import Student

class Student_repository_text_file(Student_repository):

    def __init__(self, file_name="students.txt"):
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
        try:
            file = open(self.__file_name, "r")
            line = file.readline().strip()
            while line != "":
                attributes = line.split(";")
                student = Student(int(attributes[0]), attributes[1], int(attributes[2]))
                Student_repository.add(self, student)
                line = file.readline().strip()
        except IOError as ioerror:
            raise RepositoryError(str(ioerror))
        finally:
            file.close()

    def __store_to_file(self):
        file = open(self.__file_name, "w")
        students = Student_repository.get_all(self)
        for student in students:
            store_to_file = str(student.ID) + ";" + student.name + ";" + str(student.ID) + "\n"
            file.write(store_to_file)
        file.close()