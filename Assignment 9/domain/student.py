import unittest

class Student:
    '''
    Instances of this class represent one student, having the attributes: ID, name and group
    '''
    def __init__(self, student_id, name, group):
        '''
        Constructor for Student class
        Input: student_id - the id of the student,an integer
               name - the name of the student
               group - the group to which the student belongs, an integer
        '''
        self.__ID = student_id
        self.__name = name
        self.__group = group

    @property
    def name(self):
        '''
        Getter for the name of the student
        Output: the name of the student
        '''
        return self.__name

    @name.setter
    def name(self, new_name):
        '''
        Setter for the name of the student
        return - sets the name attribute of the student to new_name
        '''
        self.__name = new_name

    @property
    def group(self):
        '''
        Getter for the group of the student
        Output: the group of the student
        '''
        return self.__group

    @group.setter
    def group(self, new_group):
        '''
        Setter for the group of the student
        :return: sets the group attribute of the student to new_group
        '''
        self.__group = new_group

    @property
    def ID(self):
        '''
        Getter for the ID of the student
        Output: the ID of the student
        '''
        return self.__ID

    def __eq__(self, other):
        '''
        Overriding the eq function.
        '''
        if isinstance(other, Student) is False:
            return False
        return self.__ID == other.__ID

    def __str__(self):
        '''
        Overriding the str function
        '''
        return "ID: " + str(self.ID) + " | Name: " + str(self.name) + " | Group: " + str(self.group)


class test_student(unittest.TestCase):

    def setUp(self):
        self.student_1 = Student(26, "Stefan", 916)
        self.student_2 = Student(26, "Radu", 916)
        self.student_3 = Student(28, "Stefan", 916)
        self.student = (28, "Stefan", 916)

    def tearDown(self):
        self.student_1 = None
        self.student_2 = None
        self.student_3 = None
        self.student = None

    def test_get_name(self):
        self.assertEqual(self.student_1.name, "Stefan")


    def test_get_group(self):
        self.assertEqual(self.student_1.group, 916)

    def test_get_ID(self):
        self.assertEqual(self.student_1.ID, 26)

    def test_eq(self):
        self.assertTrue(self.student_1 == self.student_2)
        self.assertFalse(self.student_1 == self.student_3)
        self.assertFalse(self.student == self.student_1)

    def test_str(self):
        self.assertEqual(str(self.student_1), "ID: 26 | Name: Stefan | Group: 916")

    def test_name_setter(self):
        self.student_1.name = "Radu"
        self.assertEqual(self.student_1, self.student_2)




