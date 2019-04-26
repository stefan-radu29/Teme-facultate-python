from domain.assignment import Assignment
from domain.exceptions import RepositoryError
from iterable_data_structure import My_iterable_data_structure

class Assignment_repository():
    '''
    Repository containing all the objects belonging to the Student class.
    '''

    def __init__(self):
        '''
        Constructor for the Assignment_repository class
        '''
        self._data = My_iterable_data_structure()

    def add(self, assignment):
        '''
        Adds an assignment to the repository
        student - instance of Assignment class to be added
        '''
        if assignment in self._data:
            raise RepositoryError("Assignment already exists!")
        self._data.append(assignment)

    def update(self, assignment_update):
        '''
        Updates the Assignment instance at a certain ID, by changing the description attribute and/or the deadline attribute
        assignment_update - the updated instance of Assignment having a certain ID
        '''
        assignment = self.find_one(assignment_update.ID)
        assignment.description = assignment_update.description
        assignment.deadline = assignment_update.deadline

    def remove(self, ID):
        '''
        Removes the element having the given ID from the repository.
        ID - the ID of the assignment to be removed from the repository
        '''
        assignment_to_remove = self.find_one(ID)
        self._data.remove(assignment_to_remove)

    def find_one(self, ID):
        '''
        Returns the assignment having a certain ID.
        '''
        for assignment in self._data:
            if assignment.ID == ID:
                return assignment
        raise RepositoryError("Assignment does not exist!")

    def get_all(self):
        '''
        Returns all the assignments.
        '''
        return self._data

    def __len__(self):
        '''
        Overriding the len function
        '''
        return len(self._data)