from repository.grade_repository import *
from validation.grade_validator import *
from repository.assignment_repository import *
from validation.assignment_validator import *
from validation.student_validator import *
from repository.student_repository import *
from services.student_service import Student_service
from ui.ui import Console
from services.assignment_service import Assignment_service
from services.grade_service import Grade_service
from repository.assignment_repository_text_file import Assignment_repository_text_file
from repository.assignment_repository_pickle import Assignment_repository_pickle_file
from repository.student_repository_text_file import Student_repository_text_file
from repository.student_repository_pickle import Student_repository_pickle_file
from repository.grade_repository_text_file import Grade_repository_text_file
from repository.grade_repository_pickle import Grade_repository_pickle_file

'''
Reading and applying the settings from the settings.properties file
'''
try:
    file = open("settings.properties", "r")
    line = file.readline().strip()
    option = line.split(" = ")
    if option[0] == "repository":
        if option[1] == "inmemory":
            student_repository = Student_repository()
            assignment_repository = Assignment_repository()
            grade_repository = Grade_repository()
        elif option[1] == "binaryfiles":
            for i in range(3):
                line = file.readline().strip()
                split_line = line.split(" = ")
                repository_type = split_line[0]
                repository_file = split_line[1]
                if repository_type == "students":
                    student_repository = Student_repository_pickle_file(repository_file)
                elif repository_type == "assignments":
                    assignment_repository = Assignment_repository_pickle_file(repository_file)
                elif repository_type == "grades":
                    grade_repository = Grade_repository_pickle_file(repository_file)
                else:
                    raise Exception("Invalid settings!")
        elif option[1] == "textfiles":
            for i in range(3):
                line = file.readline().strip()
                split_line = line.split(" = ")
                repository_type = split_line[0]
                repository_file = split_line[1]
                if repository_type == "students":
                    student_repository = Student_repository_text_file(repository_file)
                elif repository_type == "assignments":
                    assignment_repository = Assignment_repository_text_file(repository_file)
                elif repository_type == "grades":
                    grade_repository = Grade_repository_text_file(repository_file)
                else:
                    raise Exception("Invalid settings!")
        else:
            raise Exception("Invalid repository type in the settings.properties file!!")
    else:
        raise Exception("Invalid settings in settings.properties file!!")
except Exception as error:
    print(str(error) + "\nThe default options will be used for the settings (inmemory repositories).")
    student_repository = Student_repository()
    assignment_repository = Assignment_repository()
    grade_repository = Grade_repository()
finally:
    try:
        file.close()
    except Exception:
        pass


student_validator = Student_validator()
assignment_validator = Assignment_vaidator()
grade_validator = Grade_validator()

student_service = Student_service(student_repository, student_validator)
assignment_service = Assignment_service(assignment_repository, assignment_validator)
grade_service = Grade_service(student_repository, assignment_repository, grade_repository, grade_validator)
console = Console(student_service, assignment_service, grade_service)
console.run()
