import unittest
from datetime import *

class Assignment:
    '''
    Instances of this class represent an assignment, having the attributes id, description and deadline.
    '''
    def __init__(self, assignment_id, description, deadline):
        '''
        Constructor for Assignment class
        Input: assignment_id -  the id of the assignment, integer
               description - string
               deadline - the deadline for the assignment belonging to datetime.date class

        '''
        self.__ID = assignment_id
        self.__description = description
        self.__deadline = deadline

    @property
    def description(self):
        return self.__description

    @description.setter
    def description(self, new_description):
        self.__description = new_description

    @property
    def deadline(self):
        return self.__deadline

    @deadline.setter
    def deadline(self, new_deadline):
        self.__deadline = new_deadline

    @property
    def ID(self):
        return self.__ID

    def __eq__(self, other):
        '''
        Overriding the eq function.
        '''
        if isinstance(other, Assignment) is False:
            return False
        return self.__ID == other.__ID

    def __str__(self):
        '''
        Overriding the str function.
        '''
        return "ID: " + str(self.ID) + " | Description: " + str(self.description) + " | Deadline: " + str(self.deadline)


class test_assignment(unittest.TestCase):

    def setUp(self):
        self.assignment_1 = Assignment(20, "Best assignment ever", date(1943, 3, 13))
        self.assignment_2 = Assignment(20, "Best assignment ever", date(1943, 3, 13))
        self.assignment_3 = Assignment(30, "Best assignment ever", date(1943, 3, 13))
        self.assignment = (20, "Best assignment ever", date(1943, 3, 13))

    def tearDown(self):
        self.assignment_1 = None
        self.assignment_2 = None
        self.assignment_3 = None
        self.assignment = None

    def test_get_ID(self):
        self.assertEqual(self.assignment_1.ID, 20)

    def test_get_description(self):
        self.assertEqual(self.assignment_1.description, "Best assignment ever")

    def test_get_deadline(self):
        self.assertEqual(self.assignment_1.deadline, date(1943, 3, 13))

    def test_eq(self):
        self.assertTrue(self.assignment_1 == self.assignment_2)
        self.assertFalse(self.assignment_1 == self.assignment_3)
        self.assertFalse(self.assignment == self.assignment_1)

    def test_str(self):
        self.assertEqual(str(self.assignment_1), "ID: 20 | Description: Best assignment ever | Deadline: 1943-03-13")