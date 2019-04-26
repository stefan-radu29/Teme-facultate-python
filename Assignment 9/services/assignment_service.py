from repository.assignment_repository import *

class Assignment_service:
    '''
    Class that contains the method needed for performing the services required by the problem.
    '''

    def __init__(self, assignment_repository, assignment_validator):
        '''
        Constructor for the Assignment_service class.
        '''
        self.__assignment_repository = assignment_repository
        self.__assignment_validator = assignment_validator

    def add(self, assignment_ID, description, deadline):
        '''
        Creates, validates and adds a new assignment to the repository.
        :param assignment_ID: positive integer
        :param description: string
        :param deadline: date type
        :return:
        '''
        assignment = Assignment(assignment_ID, description, deadline)
        self.__assignment_validator.validate(assignment)
        self.__assignment_repository.add(assignment)

    def update(self, assignment_ID, new_description, new_deadline):
        '''
        Updates the assignment having a certain ID after validating the new attributes
        :param assignment_ID: positive integer
        :param new_description: string
        :param new_deadline: date type
        :return:
        '''
        new_assignment = Assignment(assignment_ID, new_description, new_deadline)
        self.__assignment_validator.validate(new_assignment)
        self.__assignment_repository.update(new_assignment)

    def remove(self, assignment_ID):
        '''
        Deletes the assignment having a certain ID from the repository.
        :param assignment_ID: positive integer
        :return:
        '''
        self.__assignment_repository.remove(assignment_ID)

    def get_all(self):
        '''
        Returns all the assignments in the repository.
        :return:
        '''
        return self.__assignment_repository.get_all()
