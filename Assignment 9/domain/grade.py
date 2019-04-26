import unittest
from domain.exceptions import ValidationError

class Grade:
    '''
    Instances of this class represent a grade, having the attributes the id of the student which receives the grade,
    the assignment for which the grade is given and the actual grade
    '''

    def __init__(self, assignment_id, student_id, grade=None):
        '''
        Constructor for Grade class
        Input: student_id - the id of the student, integer , existing student
               assignment_id - the id of the assignment being graded, integer, existing assignment
               grade - the actual grade received by the student, integer number between 0 and 10
        '''
        self.__assignment_ID = assignment_id
        self.__student_ID = student_id
        self.__numeric_value = grade

    @property
    def assignment_ID(self):
        return self.__assignment_ID

    @property
    def student_ID(self):
        return self.__student_ID

    @property
    def numeric_value(self):
        return self.__numeric_value

    @numeric_value.setter
    def numeric_value(self, new_grade):
        if self.__numeric_value is None:
            self.__numeric_value = new_grade
        else:
            raise ValidationError("An assignment can be graded only once!")

    def __eq__(self, other):
        '''
        Overriding the eq function.
        '''
        if isinstance(other, Grade) is False:
            return False
        return self.__assignment_ID == other.__assignment_ID and self.__student_ID == other.__student_ID

    def __str__(self):
        '''
        Overriding the str function.
        '''
        return "Student ID: " + str(self.student_ID) + " | Assignment ID: " + str(self.assignment_ID) + " | Grade: " + str(self.numeric_value)

class test_grade(unittest.TestCase):

    def setUp(self):
        self.grade_1 = Grade(20, 21, 9)
        self.grade_2 = Grade(12, 10, None)

    def tearDown(self):
        self.grade_1 = None
        self.grade_2 = None

    def test_get_student_ID(self):
        self.assertEqual(self.grade_1.student_ID, 21)

    def test_get_assignment_ID(self):
        self.assertEqual(self.grade_1.assignment_ID, 20)

    def test_get_grade(self):
        self.assertEqual(self.grade_1.numeric_value, 9)

    def test_set_grade(self):
        self.grade_2.numeric_value = 10
        self.assertEqual(self.grade_2.numeric_value, 10)


    def test_str(self):
        self.assertEqual(str(self.grade_1), "Student ID: 21 | Assignment ID: 20 | Grade: 9")
