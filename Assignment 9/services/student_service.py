from repository.student_repository import *


class Student_service:
    '''
    Class which contains the methods needed for performing the services required by the problem.
    '''

    def __init__(self, student_repository, student_validator):
        '''
        Constructor for the Student_service class.
        '''
        self.__student_repository = student_repository
        self.__student_validator = student_validator

    def add(self, student_ID, name, group):
        '''
        Creates, validates and adds a new student to the repository containing students
        :param student_ID: positive integer
        :param name: string
        :param group: positive integer
        '''
        student = Student(student_ID, name, group)
        self.__student_validator.validate(student)
        self.__student_repository.add(student)

    def remove(self, student_ID):
        '''
        Deletes the student having a certain ID from the repository.
        :param student_ID: positive integer
        :return:
        '''
        self.__student_repository.remove(student_ID)

    def update(self,student_ID, new_name, new_group):
        '''
        Updates the attributes of a student having a certain ID.
        :param student_ID: positive integer
        :param new_name: string
        :param new_group: positive integer
        :return:
        '''
        student_update = Student(student_ID, new_name, new_group)
        self.__student_validator.validate(student_update)
        self.__student_repository.update(student_update)

    def get_all(self):
        '''
        Returns all the students in the repository.
        :return:
        '''
        return self.__student_repository.get_all()