from repository.grade_repository import *
from datetime import date
from iterable_data_structure import gnome_sort, filter

class Grade_service:
    '''
    Class used for performing the services required by the problem.
    '''

    def __init__(self, student_repository, assignment_repository, grade_repository, grade_validator):
        '''
        Constructor for the Grade_service class.
        '''
        self.__student_repository = student_repository
        self.__assignment_repository = assignment_repository
        self.__grade_repository = grade_repository
        self.__grade_validator = grade_validator

    def give_assignment_to_student(self, student_ID, assignment_ID):
        '''
        Gives an assignment to a student.
        :param student_ID: positive integer
        :param assignment_ID: positive integer
        '''
        grade = Grade(assignment_ID, student_ID)
        self.__grade_validator.validate(grade)
        self.__assignment_repository.find_one(assignment_ID)
        self.__student_repository.find_one(student_ID)
        self.__grade_repository.add(grade)

    def give_assignment_to_group(self, group, assignment_ID):
        '''
        Gives an assignment to a group of students.
        :param group: positive integer
        :param assignment_ID: positive integer
        '''
        self.__assignment_repository.find_one(assignment_ID)
        same_group = self.__student_repository.find_group(group)
        for student in same_group:
            if self.__grade_repository.find_with_false(student.ID, assignment_ID) is False:
                grade = Grade(assignment_ID, student.ID)
                self.__grade_repository.add(grade)

    def get_all(self):
        '''
        :return: The list of all students paired with the assignments they received
        '''
        return self.__grade_repository.get_all()

    def remove_assignment(self, assignment_ID):
        '''
        Removes an assignment from the repository and all the entries in the grade repository related to that assignment.
        :param assignment_ID: positive integer
        '''
        self.__assignment_repository.remove(assignment_ID)
        grades_assignment = self.__grade_repository.find_with_assignment_ID(assignment_ID)
        for grade in grades_assignment:
            self.__grade_repository.remove(grade.student_ID, grade.assignment_ID)

    def remove_student(self, student_ID):
        '''
        Removes an assignment from the repository and all the entries in the grade repository related to that assignment.
        :param student_ID: positive integer
        '''
        self.__student_repository.remove(student_ID)
        grades_student = self.__grade_repository.find_with_student_ID(student_ID)
        for grade in grades_student:
            self.__grade_repository.remove(grade.student_ID, grade.assignment_ID)

    def get_student_assignments(self, student_ID):
        '''
        Returns all the assignments given to a student.
        :param student_ID: positive integer
        '''
        student_grades = self.__grade_repository.find_with_student_ID(student_ID)
        student_given_assignments = []
        for grade in student_grades:
            assignment = self.__assignment_repository.find_one(grade.assignment_ID)
            student_given_assignments.append(assignment)
        return student_given_assignments

    def grade_assignment(self, student_ID, assignment_ID, numeric_value_grade):
        '''
        Grades an assignment given to a student.
        :param student_ID: positive integer
        :param assignment_ID: positive integer
        '''
        grade = Grade(student_ID, assignment_ID, numeric_value_grade)
        self.__grade_validator.validate(grade)
        self.__assignment_repository.find_one(assignment_ID)
        self.__student_repository.find_one(student_ID)
        self.__grade_repository.update(student_ID, assignment_ID, numeric_value_grade)

    def get_students_for_assignment_sorted(self, assignment_ID):
        '''
        Returns all students who received a given assignment, ordered alphabetically.
        :param assignment_ID: positive integer
        '''
        self.__assignment_repository.find_one(assignment_ID)
        students = []
        grades = self.__grade_repository.find_with_assignment_ID(assignment_ID)
        for grade in grades:
            student = self.__student_repository.find_one(grade.student_ID)
            students.append(student)
        if len(students) == 0:
            return students
        #students.sort(key=lambda x: x.name)
        '''###Using gnome sort###'''
        gnome_sort(students, lambda student: student.name)
        return students[:]

    def get_students_who_are_late(self):
        '''
        Returns all students who are late in handing in at least one assignment.
        :return:
        '''
        today = date.today()
        grades = self.__grade_repository.get_all()
        ungraded_given_assignments = []
        #for grade in grades:
        #    if grade.numeric_value is None and (self.__assignment_repository.find_one(grade.assignment_ID)).deadline < today:
        #       ungraded_given_assignments.append(grade)
        '''###Using implemented filter###'''
        ungraded_given_assignments = filter(grades, lambda grade: grade.numeric_value is None and (self.__assignment_repository.find_one(grade.assignment_ID)).deadline < today)
        students_ungraded = []
        for grade in ungraded_given_assignments:
            student = self.__student_repository.find_one(grade.student_ID)
            if student not in students_ungraded:
                students_ungraded.append(student)
        return students_ungraded[:]

    def get_students_best_school_situation(self):
        '''
        Returns the students with the best school situation, sorted in descending order of the average grade received for
        all assignments.
        :return:
        '''
        students = self.__student_repository.get_all()
        grades = self.__grade_repository.get_all()
        students_and_averages = {}
        for student in students:
            number_of_grades = 0
            sum_of_grades = 0
            for grade in grades:
                if student.ID == grade.student_ID and grade.numeric_value is not None:
                    sum_of_grades = sum_of_grades + grade.numeric_value
                    number_of_grades = number_of_grades + 1
            if number_of_grades == 0:
                average = 0/1
            else:
                average = sum_of_grades / number_of_grades
            students_and_averages[str(student)] = average
        sorted_students_and_averages = sorted(students_and_averages.items(), key=lambda kv: kv[1], reverse=True)
        return sorted_students_and_averages[:]

    def get_assignments_at_least_one_grade(self):
        '''
        All assignments for which there is at least one grade, sorted in descending order of the average grade received
        by all students who received that assignment.
        :return:
        '''
        assignments = self.__assignment_repository.get_all()
        grades = self.__grade_repository.get_all()
        assignments_and_averages = {}
        for assignment in assignments:
            number_of_grades = 0
            sum_of_grades = 0
            for grade in grades:
                if assignment.ID == grade.assignment_ID and grade.numeric_value is not None:
                    sum_of_grades = sum_of_grades + grade.numeric_value
                    number_of_grades = number_of_grades + 1
            if number_of_grades != 0:
                average = sum_of_grades / number_of_grades
                assignments_and_averages[str(assignment)] = average
        sorted_assignments_and_averages = sorted(assignments_and_averages.items(), key=lambda kv: kv[1], reverse=True)
        return sorted_assignments_and_averages[:]
