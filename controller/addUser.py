#!/usr/local/bin/python3

"""
created_by:         Keshav Patel
created_date:       3/4/2015
last_modified_by:   Ebube Chuba
last_modified date: 3/6/2015
"""

# imports
import constants
import utils
import json
from sql.user import User

#Format of assessment -AM
#requestType: addUser
#username: "string"
#password: "string"
#firstName: "string"
#lastName: "string"
#role: []

def iChooseU(json):
    thisUser = utils.findUser(json)

    username = json.getlist("username")
    password = json.getlist("password")
    firstName = json.getlist("firstName")
    lastName = json.getlist("lastName")
    role = json.getlist("role")

    addAssessment = 0
    editUser = 0
    editQuestion = 0
    editAnswer = 0
    editTestCase = 0
    editPermission = 0
    viewStudentInfo = 0
    viewTeacherInfo = 0
    viewAnswer = 0
    viewTestCase = 0
    viewQuestion = 0
    viewAllQuestion = 0

    if "Admin" in role:
        editUser = 1
        editPermission = 1
        viewTeacherInfo = 1
    if "Teacher" in role:
        addAssessment = 1
        editQuestion = 1
        editAnswer = 1
        editTestCase = 1
        viewStudentInfo = 1
        viewAnswer = 1
        viweTestCase = 1
        viewQuestion = 1
        viewAllQuestion = 1
    if "TA" in role:
        viewStudentInfo = 1
        viewAnswer = 1
        viewTestCase = 1
        viewQuestion = 1
        viewAllQuestion = 1
    if "Student" in role:
        editAnswer = 1
        viewAnswer = 1
        viewQuestion = 1

    newUser = User.noID(None, thisUser, None, username, password, firstName, lastName, role, addAssessment, editUser, editQuestion, editAnswer, editTestCase, editPermission, viewStudentInfo, viewTeacherInfo, viewAnswer, viewTestCase, viewQuestion, viewAllQuestion, constants.ACTIVE)
    newUser.add()

    return utils.successJson(json)
