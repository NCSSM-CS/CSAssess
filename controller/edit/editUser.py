#!/usr/bin/python

"""
created_by:         Aninda Manocha
created_date:       3/2/2015
last_modified_by:   Aninda Manocha
last_modified date: 3/2/2015
"""

# imports

def newUser(created_by, username, password, first_name, last_name, role)
    """
    created_by - the user who created the new user
    username   - the username of the new user
    password   - the hashed password of the new user 
    first_name - the first name of the new user
    last_name  - the last name of the new user
    role       - the role of the new user

    This function creates a new user with a given name, username, and password.
    """

    if role == "student": 
        add_assessment = 0 
        edit_user = 0
        edit_question = 0
        edit_answer = 1
        edit_test_case = 0
        edit_permission = 0
        view_student_info = 0
        view_teacher_info = 0
        view_answer = 1
        view_test_case = 0
        view_question = 1
        view_all_question = 0
    elif role == "teacher":
        add_assessment = 1
        edit_user = 0
        edit_question = 1
        edit_answer = 1
        edit_test_case = 1
        edit_permission = 0
        view_student_info = 1
        view_teacher_info = 0
        view_answer = 1
        view_test_case = 1
        view_question = 1
        view_all_question = 1
    elif role == "admin":
        add_assessment = 0
        edit_user = 1
        edit_question = 0
        edit_answer = 0
        edit_test_case = 0
        edit_permission = 1
        view_student_info = 1
        view_teacher_info = 1
        view_answer = 0
        view_test_case = 0
        view_question = 0
        view_all_question = 0
    else:
        print("TODO: HANDLE THIS ERROR")

    newUser = User.noID(time.strftime("%Y-%m-%d %H:%M:%S"), created_by, time.strftime("%Y-%m-%d %H:%M:%S"), last_login, username, password, first_name, last_name, role, add_assessment, edit_user, edit_question, edit_answer, edit_test_case, edit_permission, view_student_info, view_teacher_info, view_answer, view_test_case, view_question, view_all_question)
    addUser(newUser) #add new user to database 

def addUser(user):
    """
    user - the new user being added to the database

    This function takes a new user and adds him/her to the database.
    """ 

   #MODEL TEAM: write SQL code for adding to database
