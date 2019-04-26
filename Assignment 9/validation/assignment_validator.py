from domain.assignment import *
from domain.exceptions import ValidationError

class Assignment_vaidator:


    def validate(self, assignment):
        '''
        Check whether the provided instance of Assignment is valid or not.
        assignment - instance of Assignment type
        return - raises assignment_exception if there there are validation errors or returns true if there are no validation errors
        '''
        if isinstance(assignment, Assignment) == False:
            raise TypeError("Not an assignment!")
        __errors = ""
        now = date.today()
        if assignment.ID < 0:
            __errors += ("Assignment ID must be a positive integer!")
        if assignment.deadline.year > 2019:
            __errors += ("\nThe assignment's deadline cannot exceed the year 2019!")
        if len(__errors) != 0:
            raise ValidationError(__errors)
        return True

class test_Assignment_validator(unittest.TestCase):

    def setUp(self):
        self.validator = Assignment_vaidator()
        self.assignment1 = (12, "description", date(2018, 11, 23))
        self.assignment2 = Assignment("12", "description", date(2018, 11, 23))
        self.assignment3 = Assignment(12, ["description"], date(2018, 11, 23))
        self.assignment4 = Assignment(12, "description", (2018, 11, 23))
        self.assignment5 = Assignment(12, "description", date(2020, 11, 23))
        self.assignment6 = Assignment(12, "description", date(2018, 10, 23))
        self.assignment7 = Assignment("12", ["description"], date(2018, 11, 21))
        self.assignment8 = Assignment(12, "description", date(2018, 11, 30))

    def tearDown(self):
        self.validator = None
        self.assignment1 = None
        self.assignment2 = None
        self.assignment3 = None
        self.assignment4 = None
        self.assignment5 = None
        self.assignment6 = None
        self.assignment7 = None
        self.assignment8 = None

    def test_validate(self):
        with self.assertRaises(TypeError):
            self.validator.validate(self.assignment1)
        with self.assertRaises(TestError):
            self.validator.validate(self.assignment2)
        with self.assertRaises(RepositoryError):
            self.validator.validate(self.assignment3)
        with self.assertRaises(RepositoryError):
            self.validator.validate(self.assignment4)
        with self.assertRaises(RepositoryError):
            self.validator.validate(self.assignment5)
        with self.assertRaises(RepositoryError):
            self.validator.validate(self.assignment6)
        with self.assertRaises(RepositoryError):
            self.validator.validate(self.assignment7)
        self.assertTrue(self.validator.validate(self.assignment8))