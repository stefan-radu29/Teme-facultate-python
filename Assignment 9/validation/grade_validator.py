from domain.grade import *
from domain.exceptions import ValidationError

class Grade_validator:

    def validate(self, grade):
        '''
        Checks whether the provided instance of a Grade is valid or not.
        grade - instance of Grade class
        return - raises student_exception if there there are validation errors or returns true if there are no validation errors
        '''
        if isinstance(grade, Grade) == False:
            raise TypeError("Not a grade!")
        __errors = ""
        if grade.assignment_ID < 0:
            __errors += ("\nAssignment ID must be a positive integer!")
        if grade.student_ID < 0:
            __errors += ("\nStudent ID must be a positive integer!")
        if grade.numeric_value is not None and (grade.numeric_value < 0 or grade.numeric_value > 10):
            __errors += ("\nThe grade for an assignment must be an integer between 0 and 10!")
        if len(__errors) != 0:
            raise ValidationError(__errors)
        return True
