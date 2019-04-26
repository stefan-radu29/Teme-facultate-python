from domain.student import *
from domain.exceptions import ValidationError

class Student_validator:

    def validate(self, student):
        '''
        Check whether the provided instance of Student is valid or not.
        student - instance of Student type
        return - raises student_exception if there there are validation errors or returns true if there are no validation errors
        '''
        errors = ''
        if isinstance(student, Student) == False:
            raise TypeError("Not a student!")
        name = student.name.split()
        if len(name) < 2:
            errors += ("The name of the student must be composed of a first name and a last name!")
        if student.ID < 0:
            errors += ("\nThe ID must be a positive integer!")
        if student.group < 0:
            errors += ("\nThe group must be a positive integer!")
        if len(errors) > 0:
            raise ValidationError(errors)
        return True

class test_Student_validator(unittest.TestCase):

    def setUp(self):
        self.validator = Student_validator()
        self.student1 = Student('1t', "Mihai Andrei", 916)
        self.student2 = Student(11, "mihai", 916 )
        self.student3 = [11, "stefan radu", 916]
        self.student4 = Student(20, "Pop Alex", "91t")
        self.student5 = Student('1t', "Mihai", "916o")
        self.student6 = Student(12, "Pop Ioan Mihai", 111)
        self.student7 = Student('', '', '')
        self.student8 = Student(12, '', 132)
        self.student9 = Student(-12, '', 132)

    def tearDown(self):
        self.validator = None
        self.student1 = None
        self.student2 = None
        self.student3 = None
        self.student4 = None
        self.student5 = None
        self.student6 = None
        self.student7 = None
        self.student8 = None
        self.student9 = None

    def test_validate(self):
        with self.assertRaises(ValidationError):
            self.validator.validate(self.student1)
        with self.assertRaises(ValidationError):
            self.validator.validate(self.student2)
        with self.assertRaises(TypeError):
            self.validator.validate(self.student3)
        with self.assertRaises(ValidationError):
            self.validator.validate(self.student4)
        with self.assertRaises(ValidationError):
            self.validator.validate(self.student5)
        self.assertTrue(self.validator.validate(self.student6))
        with self.assertRaises(ValidationError):
            self.validator.validate(self.student7)
        with self.assertRaises(ValidationError):
            self.validator.validate(self.student8)
        self.validator.validate(self.student9)