from domain.exceptions import *
from datetime import *


class Console:

    def __init__(self, student_service, assignment_service, grade_service):
        self.__student_service = student_service
        self.__assignment_service = assignment_service
        self.__grade_service = grade_service
        self.__main_menu = "\nChoose one of the following options by typing the corresponding digit and pressing Enter:\n" \
                           "1. Perform operations with the repository containing students.\n" \
                           "2. Perform operations with the repository containing assignments.\n" \
                           "3. Give assignment to a student or a group of students.\n" \
                           "4. Grade student for a given assignment.\n" \
                           "5. List given assignments and grades.\n" \
                           "6. Create statistics.\n" \
                           "7. Undo.\n" \
                           "8. Redo.\n" \
                           "9. Exit.\n"
        self.__menu_1 = "\nChoose one of the following options by typing the corresponding digit and pressing Enter:\n" \
                        "1. Add a student.\n" \
                        "2. Remove a student.\n" \
                        "3. Update a student.\n" \
                        "4. List all students.\n" \
                        "5. Back."
        self.__menu_2 = "\nChoose one of the following options by typing the corresponding digit and pressing Enter:\n" \
                        "1. Add an assignment.\n" \
                        "2. Remove an assignment.\n" \
                        "3. Update an assignment.\n" \
                        "4. List all assignments.\n" \
                        "5. Back."
        self.__menu_3 = "\nChoose one of the following options by typing the corresponding digit and pressing Enter:\n" \
                        "1. Give assignment to a student.\n" \
                        "2. Give assignment to a group of students.\n" \
                        "3. Back."
        self.__menu_6 = "\nChoose one of the following options by typing the corresponding digit and pressing Enter:\n" \
                        "1. All students who received a given assignment, ordered alphabetically.\n" \
                        "2. All students who are late in handling in at least one assignment.\n" \
                        "3. Students with the best school situation, sorted in descending order of the average grade" \
                        "received for all assignments.\n" \
                        "4. All assignments for which there is at least one grade, sorted in descending order of the " \
                        "average grade received by all students who received that assignment.\n" \
                        "5. Back."

    def run(self):
        while True:
            print(self.__main_menu)
            try:
                choice = int(input())
                if choice > 9 or choice < 1:
                    raise ValueError("Invalid choice!")
                if choice == 1:
                    self.__option_1()
                elif choice == 2:
                    self.__option_2()
                elif choice == 3:
                    self.__option_3()
                elif choice == 4:
                    self.__option_4()
                elif choice == 5:
                    self.__option_5()
                elif choice == 6:
                    self.__option_6()
                elif choice == 9:
                    return
            except ValueError as value_error:
                print("\nValue Error:\n")
                print(value_error)
            except ValidationError as validation_error:
                print("\nValidation Error:\n")
                print(validation_error)
            except RepositoryError as repository_error:
                print("\nRepository Error:\n")
                print(repository_error)

    def __option_1(self):
        while True:
            print(self.__menu_1)
            choice = int(input())
            if choice > 5 or choice < 1:
                raise ValueError("Invalid choice!")
            if choice == 1:
                self.__UI_add_student()
            elif choice == 2:
                self.__UI_remove_student()
            elif choice == 3:
                self.__UI_update_student()
            elif choice == 4:
                self.__UI_list_students()
            elif choice == 5:
                return

    def __option_2(self):
        while True:
            print(self.__menu_2)
            choice = int(input())
            if choice > 5 or choice < 1:
                raise ValueError("Invalid choice!")
            if choice == 1:
                self.__UI_add_assignment()
            elif choice == 2:
                self.__UI_remove_assignment()
            elif choice == 3:
                self.__UI_update_assignment()
            elif choice == 4:
                self.__UI_list_assignments()
            elif choice == 5:
                return

    def __option_3(self):
        while True:
            print(self.__menu_3)
            choice = int(input())
            if choice > 3 or choice < 1:
                raise ValueError("Invalid choice!")
            if choice == 1:
                self.__UI_give_assignment_to_student()
            elif choice == 2:
                self.__UI_give_assignment_to_group()
            elif choice == 3:
                return

    def __option_4(self):
        print("Student ID: ", end="")
        student_ID = int(input())
        student_given_assignments= self.__grade_service.get_student_assignments(student_ID)
        if len(student_given_assignments) == 0:
            print("This student received no assignment!")
        else:
            print("The assignments given to this student are: ")
            for given_assignment in student_given_assignments:
                print(given_assignment)
            print("Assignment ID(the assignment which needs to be graded): ",end='')
            assignment_ID = int(input())
            print("Grade: ", end='')
            numeric_value_grade = int(input())
            self.__grade_service.grade_assignment(student_ID, assignment_ID, numeric_value_grade)

    def __option_5(self):
        self.__UI__list_grades()

    def __option_6(self):
        while True:
            print(self.__menu_6)
            choice = int(input())
            if choice > 5 or choice < 1:
                raise ValueError("Invalid choice!")
            if choice == 1:
                self.__UI_statistic_student_received_assignment()
            elif choice == 2:
                self.__UI_statistic_students_late_handing_in()
            elif choice == 3:
                self.__UI_statistic_best_school_situation()
            elif choice == 4:
                self. __UI_statistic_assignments_ordered_by_average_grade()
            elif choice == 5:
                return


    def __UI_add_student(self):
        print("ID: ", end='')
        student_ID = int(input())
        print("Name: ", end='')
        name = input()
        print("Group: ", end='')
        group = int(input())
        self.__student_service.add(student_ID, name, group)

    def __UI_remove_student(self):
        print("ID: ", end='')
        student_ID = int(input())
        self.__grade_service.remove_student(student_ID)

    def __UI_update_student(self):
        print("ID: ", end='')
        student_ID = int(input())
        print("New Name: ", end='')
        new_name = input()
        print("New Group: ", end='')
        new_group = int(input())
        self.__student_service.update(student_ID, new_name, new_group)

    def __UI_list_students(self):
        students = self.__student_service.get_all()
        if len(students) == 0:
            print("There are no students!")
        else:
            for student in students:
                print(student)



    def __UI_add_assignment(self):
        print("ID: ", end="")
        assignment_ID = int(input())
        print("Description: ", end="")
        description = input()
        print("Deadline(YYYY MM DD): ", end="")
        deadline_string = input()
        deadline_split = deadline_string.split(' ')
        if len(deadline_split) != 3:
            raise ValueError("Invalid data format!")
        deadline = date(int(deadline_split[0]), int(deadline_split[1]), int(deadline_split[2]))
        self.__assignment_service.add(assignment_ID, description, deadline)

    def __UI_remove_assignment(self):
        print("ID: ", end="")
        assignment_ID = int(input())
        self.__grade_service.remove_assignment(assignment_ID)

    def __UI_update_assignment(self):
        print("ID: ", end="")
        assignment_ID = int(input())
        print("Description: ", end="")
        new_description = input()
        print("Deadline(YYYY MM DD): ", end="")
        deadline_string = input()
        deadline_split = deadline_string.split(' ')
        if len(deadline_split) != 3:
            raise ValueError("Invalid data format!")
        new_deadline = date(int(deadline_split[0]), int(deadline_split[1]), int(deadline_split[2]))
        self.__assignment_service.update(assignment_ID, new_description, new_deadline)

    def __UI_list_assignments(self):
        assignments = self.__assignment_service.get_all()
        if len(assignments) == 0:
            print("There are no assignments!")
        else:
            for assignment in assignments:
                print(assignment)



    def __UI_give_assignment_to_student(self):
        print("Student ID: ", end='')
        student_ID = int(input())
        print("Assignment ID: ", end='')
        assignment_ID = int(input())
        self.__grade_service.give_assignment_to_student(student_ID, assignment_ID)

    def __UI_give_assignment_to_group(self):
        print("Group: ", end='')
        group = int(input())
        print("Assignment ID: ", end='')
        assignment_ID = int(input())
        self.__grade_service.give_assignment_to_group(group, assignment_ID)

    def __UI__list_grades(self):
        all_grades = self.__grade_service.get_all()
        if len(all_grades) == 0:
            print("There are no assignments given or graded!")
        else:
            for grade in all_grades:
                print(grade)


    def __UI_statistic_student_received_assignment(self):
        print("Assignment ID: ", end='')
        assignment_ID = int(input())
        students = self.__grade_service.get_students_for_assignment_sorted(assignment_ID)
        if len(students) == 0:
            print("\nThere are no students who received this assignment!")
        else:
            print("All students who received this assignment, ordered alphabetically:\n")
            for student in students:
                print(student)

    def __UI_statistic_students_late_handing_in(self):
        students_late_handing_in = self.__grade_service.get_students_who_are_late()
        if len(students_late_handing_in) == 0:
            print("\nThere are no students who are late in handing in at least one assignment!")
        else:
            print("Students who are late handing in at least one assignment are:\n")
            for student in students_late_handing_in:
                print(student)

    def __UI_statistic_best_school_situation(self):
        students_best_school_situation = self.__grade_service.get_students_best_school_situation()
        if len(students_best_school_situation) == 0:
            print("There are no students!")
        else:
            print("Students with the best school situation, sorted in descending order of the average grade received\n"
                  "for all assignments are:")
            print("Average grade        Student")
            for student in students_best_school_situation:
                print(str(student[1]) + '                     ' + str(student[0]))

    def __UI_statistic_assignments_ordered_by_average_grade(self):
        assignments_ordered_by_average_grade = self.__grade_service.get_assignments_at_least_one_grade()
        if len(assignments_ordered_by_average_grade) == 0:
            print("There are no graded assignments!")
        else:
            print("All assignments for which there is at least one grade, sorted in descending order of the average\n"
                  "grade received by all students who received that assignment are:")
            print("Average grade        Assignment")
            for assignment in assignments_ordered_by_average_grade:
                print(str(assignment[1]) + '                     ' + str(assignment[0]))









