from domain.exceptions import RepositoryError
from domain.grade import Grade
from iterable_data_structure import My_iterable_data_structure

class Grade_repository:
    '''
    Repository for all the objects belonging to the Grade class.
    '''

    def __init__(self):
        '''
        Constructor for the Grade_repository class.
        '''
        self._data = My_iterable_data_structure()

    def add(self, grade):
        '''
        Adds a new grade to the repository.
        :param grade - instance of Grade class
        '''
        if grade in self._data:
            raise RepositoryError("This assignment already given to this student!")
        self._data.append(grade)

    def remove(self, student_ID, assignment_ID):
        '''
        Removes a grade from the repository.
        '''
        grade_to_remove = self.find(student_ID, assignment_ID)
        self._data.remove(grade_to_remove)

    def update(self, student_ID, assignment_ID, numeric_value_grade):
        '''
        Updates a grade by changing the numeric value of the grade.
        :param student_ID:
        :param assignment_ID:
        :param numeric_value_grade: integer between 0 and 10
        :return:
        '''
        grade_to_update = self.find(student_ID, assignment_ID)
        grade_to_update.numeric_value = numeric_value_grade


    def find_with_student_ID(self, student_ID):
        '''
        Returns all the assignments given to a certain student.
        '''
        grades_student = []
        for grade in self._data:
            if grade.student_ID == student_ID:
                grades_student.append(grade)
        return grades_student

    def find_with_assignment_ID(self, assignment_ID):
        '''
        Returns all the grades for the students that have received a certain assignment.
        '''
        grades_assignment = []
        for grade in self._data:
            if grade.assignment_ID == assignment_ID:
                grades_assignment.append(grade)
        return grades_assignment

    def find(self, student_ID, assignment_ID):
        '''
        Returns the grade a student received for an assignment.
        '''
        for grade in self._data:
            if grade.assignment_ID == assignment_ID and grade.student_ID == student_ID:
                return grade
        raise RepositoryError("Assignment not given to this student!")

    def find_with_false(self, student_ID, assignment_ID):
        '''
        Returns the grade a student received for an assignment.
        '''
        for grade in self._data:
            if grade.assignment_ID == assignment_ID and grade.student_ID == student_ID:
                return grade
        return False

    def get_all(self):
        '''
        Returns all the grades.
        '''
        return self._data