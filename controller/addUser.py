#!/usr/bin/python3

"""
created_by:         Keshav Patel
created_date:       3/4/2015
last_modified_by:   Keshav Patel
last_modified date: 3/4/2015
"""

# imports
import constants
import utils
import json
from sql.session import Session

#Format of assessment -KP
#requestType: addUser
#last_login        - the date when the user 'self' was last logged in
#username          - the username of the user 'self'
#password          - the hashed password of the user 'self'
#first_name        - the first name of the user 'self'
#last_name         - the last name of the user 'self'
#role              - the role of the user 'self'
#add_assessment    - whether the user 'self' can add assignments or not
#edit_user         - whether the user 'self' can edit users or not
#edit_question     - whether the user 'self' can edit questions or not
#edit_answer       - whether the user 'self' can edit answers or not
#edit_test_case    - whether the user 'self' can edit test cases or not
#edit_permission   - whether the user 'self' can edit permissions or not
#view_student_info - whether the user 'self' can view student information or not
#view_teacher_info - whether the user 'self' can view teacher information or not
#view_answer       - whether the user 'self' can view answers or not
#view_test_case    - whether the user 'self' can view test cases or not
#view_question     - whether the user 'self' can view questions or not
#view_all_question - whether the user 'self' can view all questions or not


def iChooseU(json):
    thisUser = findUser()

    username = json["username"]
    password = json["password"]
    firstName = json["firstName"]
    lastName = json["lastName"]
    role = json["role"]
    addAssessment = json["addAssessment"]
    editUser = json["editUser"]
    editQuestion = json["editQuestion"]
    editAnswer = json["editAnswer"]
    editTestCase = json["editTestCase"]
    editPermission = json["editPermission"]
    viewStudentInfo = json["viewStudentInfo"]
    viewTeacherInfo = json["viewTeacherInfo"]
    viewAnswer = json["viewAnswer"]
    viewTestCase = json["viewTestCase"]
    viewQuestion = json["viewQuestion"]
    viewAllQuestion = json["viewAllQuestion"]

    newUser = User.noID(None, thisUser, 0, username, password, firstName, lastName, role, addAssessment, editUser, editQuestion, editAnswer, editTestCase, editPermission, viewStudentInfo, viewTeacherInfo, viewAnswer, viewTestCase, viewQuestion, viewAllQuestion, ACTIVE)
    newUser.add()

    successJson()
