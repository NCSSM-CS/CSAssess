#!/usr/bin/python

'''
created_by:         Micah Halter
created_date:       3/1/2015
last_modified_by:   Micah Halter
last_modified date: 3/1/2015
'''

# imports
import constants
import sys

from user import User

import mysql.connector
from mysql_connect_config import getConfig


# functions
def all():
    """
    returns a list of all of the users stored on the database

    this function allows for viewing of every user in the database
    """

    cnx = mysql.connector.connect(**getConfig("csassess"))
    cursor = cnx.cursor()

    # gets all of the user ids stored on the database
    userView = (
            "SELECT u.id "
            "FROM user AS u;")

    cursor.execute(userView)

    # for every user id, it created a user object and
    # adds it to a list to return
    user_list = list()
    for (id) in cursor:
        user_list.append(byID(id))

    return user_list

def byID(userId):
    """
    userId - the id number of the course that is wanting to be viewed

    returns a user object that has the id of the userId in the database

    this function allows for viewing of a user in the database
    """

    cnx = mysql.connector.connect(**getConfig("csassess"))
    cursor = cnx.cursor()

    # gets all of the metadata of the user at the id 'userId'
    userView = (
            "SELECT u.* "
            "FROM user AS u "
            "WHERE u.id=%s;" % userId)

    cursor.execute(userView)

    # assigns the needed values to create a new user object
    # and grabs them from the database
    id = ""
    created = ""
    created_by = ""
    last_login = ""
    username = ""
    password = ""
    first_name = ""
    last_name = ""
    role = ""
    add_assessment = ""
    edit_user = ""
    edit_question = ""
    edit_answer = ""
    edit_test_case = ""
    edit_permission = ""
    view_student_info = ""
    view_teacher_info = ""
    view_answer = ""
    view_test_case = ""
    view_question = ""
    view_all_question = ""


    for (cid, ccreated, ccreatedBy, clastLogin, cusername, cpassword, cfirstName, clastName, crole, caddAssessment, ceditUser, ceditQuestion, ceditAnswer, ceditTestCase, ceditPermission, cviewStudentInfo, cviewTeacherInfo, cviewAnswer, cviewTestCase, cviewQuestion, cviewAllQuestion) in cursor:
        id = cid
        created = ccreated
        created_by = ccreatedBy
        last_login = clastLogin
        username = cusername
        password = cpassword
        first_name = cfirstName
        last_name = clastName
        role = crole
        add_assessment = caddAssessment
        edit_user = ceditUser
        edit_question = ceditQuestion
        edit_answer = ceditAnswer
        edit_test_case = ceditTestCase
        edit_permission = ceditPermission
        view_student_info = cviewStudentInfo
        view_teacher_info = cviewTeacherInfo
        view_answer = cviewAnswer
        view_test_case = cviewTestCase
        view_question = cviewQuestion
        view_all_question = cviewAllQuestion

    # calls the byId method if the user wasn't created by themselves
    # if the user was created by itself, then it sets the created_by
    # variable to the username
    return User(id, created, username if created_by == id else byID(created_by), last_login, username, password, first_name, last_name, role, add_assessment, edit_user, edit_question, edit_answer, edit_test_case, edit_permission, view_student_info, view_teacher_info, view_answer, view_test_case, view_question, view_all_question)
