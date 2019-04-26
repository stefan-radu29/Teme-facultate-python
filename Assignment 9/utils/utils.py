'''
Module containing utility functions
'''
from random import choice
from datetime import date


def populate_students():
    data = []
    groups = [916, 917, 918]
    first_names = ["alexandru", "ioana", "catalin", "george", "vasile", "ioan", "cristina", "maria", "stefan", "andrei", "gheorghe", "cornel", "denisa", "andreea"]
    last_names = ["pop", "popescu", "georgescu", "badea", "olareanu", "ion", "matei" , "grigore"]
    for i in range(10):
        student_full_name = choice(last_names) + ' ' + choice(first_names)
        group = choice(groups)
        student = (i+1, student_full_name, group)
        data.append(student)
    return data

def populate_assignments():
    data = []
    description = ["algebra", "calculus", "fundamentals of programming", "computational logic", "asc"]
    days = [10, 14, 23, 17]
    for i in range(5):
        full_description = choice(description) + " homework"
        deadline = date(2018, 12, choice(days))
        assignment_data = (i+1, full_description, deadline)
        data.append(assignment_data)
    return data

def populate_grades():
    data = []
    for i in range(5):
        grade = (choice([1,2,3,4,5,6,7,8,9,10]), choice([1,2,3,4,5]), choice([1,2,3,4,5,6,7,8,9,10]))
        data.append(grade)
    return data
