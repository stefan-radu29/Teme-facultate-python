import unittest
from domain.student import Student
from domain.exceptions import RepositoryError
from iterable_data_structure import My_iterable_data_structure

class Student_repository():
    '''
    Instances of this class represent a repository containing all the objects belonging to the Student class.
    '''

    def __init__(self):
        '''
        Constructor for the Student_repository class
        '''
        self._data = My_iterable_data_structure()

    def add(self, student):
        '''
        Adds a student to the repository
        student - instance of Student class to be added
        '''
        if student in self._data:
            raise RepositoryError("Student already exists!")
        self._data.append(student)

    def update(self, student_update):
        '''
        Updates the Student instance at a certain ID, by changing the Name attribute and/or the Group attribute
        student_update - the updated instance of Student having a certain ID
        '''
        student = self.find_one(student_update.ID)
        student.group = student_update.group
        student.name = student_update.name


    def remove(self, ID):
        '''
        Removes the element having the given ID from the repository.
        ID - the ID of the student to be removed from the repository
        '''
        student_to_remove = self.find_one(ID)
        self._data.remove(student_to_remove)

    def find_one(self, ID):
        '''
        Returns the student having a certain ID.
        '''
        for student in self._data:
            if student.ID == ID:
                return student
        raise RepositoryError("Student does not exist!")

    def find_group(self, group):
        '''
        Returns the students belonging to the same group
        '''
        same_group = []
        for student in self._data:
            if student.group == group:
                same_group.append(student)
        if len(same_group) == 0:
            raise RepositoryError("Group does not exit!")
        else:
            return same_group

    def get_all(self):
        '''
        Returns all the students
        '''
        return self._data


    def __len__(self):
        '''
        Overriding the len function
        '''
        return len(self._data)

class test_Student_repository(unittest.TestCase):
    def setUp(self):
        self.repo = Student_repository()
        self.student1 = Student(11, "Tadu Stefan", 916)
        self.student2 = Student(12, "Pop Ion", 917)
        self.student3 = Student(11, "marcel grigore", 920)
        self.student4 = Student(13, "marcel popescu", 916)

    def tearDown(self):
        self.repo = None
        self.student1 = None
        self.student2 = None
        self.student3 = None
        self.student4 = None

    def test_add(self):
        self.assertEqual(len(self.repo), 0)
        self.repo.add(self.student1)
        self.assertEqual(len(self.repo), 1)
        self.repo.add(self.student2)
        self.assertEqual(len(self.repo), 2)

    def test_find_group(self):
        self.repo.add(self.student1)
        self.repo.add(self.student2)
        self.repo.add(self.student4)
        same_group = self.repo.find_group(916)
        self.assertEqual(same_group, [self.student1, self.student4])
        same_group = self.repo.find_group(917)
        self.assertEqual(same_group, [self.student2])
        self.assertFalse(self.repo.find_group(930))

    def test_remove(self):
        self.repo.add(self.student1)
        self.repo.add(self.student2)
        self.repo.add(self.student4)
        self.assertEqual(len(self.repo), 3)
        self.repo.remove(12)
        self.assertEqual(len(self.repo), 2)
        self.assertEqual(self.repo._data, [self.student1, self.student4])

    def test_find_one(self):
        self.repo.add(self.student1)
        self.repo.add(self.student2)
        self.repo.add(self.student4)
        self.assertEqual(self.repo.find_one(12), self.student2)
        self.assertEqual(self.repo.find_one(13), self.student4)
        self.assertFalse(self.repo.find_one(20))

    def test_update(self):
        self.repo.add(self.student1)
        self.repo.add(self.student2)
        self.repo.add(self.student4)
        new_student = Student(12, "Radu Stefan", 918)
        self.repo.update(new_student)
        self.assertEqual(self.repo._data, [self.student1, new_student, self.student4])
        new_student2 = Student(13, "Ion Cristian Mihai", 999)
        self.repo.update(new_student2)
