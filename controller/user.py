#!/usr/bin/python

"""
created_by:         Micah Halter
created_date:       3/1/2015
last_modified_by:   John Fang
last_modified date: 3/2/2015
"""

# imports
import constants
import json

# classes
class User:
    'Assessment object to hold attributes and functions for an assessment'

    def __init__(self, id, created, created_by, last_login, username, password, first_name, last_name, role, add_assessment, edit_user, edit_question, edit_answer, edit_test_case, edit_permission, view_student_info, view_teacher_info, view_answer, view_test_case, view_question, view_all_question):
        """
        self              - the user in question
        id                - the id number of the user 'self' in the database
        created           - the date when the user 'self' was created
        created_by        - the user that created the user 'self'
        last_login        - the date when the user 'self' was last logged in
        username          - the username of the user 'self'
        password          - the hashed password of the user 'self'
        first_name        - the first name of the user 'self'
        last_name         - the last name of the user 'self'
        role              - the role of the user 'self'
        add_assessment    - whether the user 'self' can add assignments or not
        edit_user         - whether the user 'self' can edit users or not
        edit_question     - whether the user 'self' can edit questions or not
        edit_answer       - whether the user 'self' can edit answers or not
        edit_test_case    - whether the user 'self' can edit test cases or not
        edit_permission   - whether the user 'self' can edit permissions or not
        view_student_info - whether the user 'self' can view student information or not
        view_teacher_info - whether the user 'self' can view teacher information or not
        view_answer       - whether the user 'self' can view answers or not
        view_test_case    - whether the user 'self' can view test cases or not
        view_question     - whether the user 'self' can view questions or not
        view_all_question - whether the user 'self' can view all questions or not

        this function acts as the constructor to define a new user object
        """
        self.id                = id
        self.created           = created
        self.created_by        = created_by
        self.last_login        = last_login
        self.username          = username
        self.password          = password
        self.first_name        = first_name
        self.last_name         = last_name
        self.role              = role
        self.add_assessment    = add_assessment
        self.edit_user         = edit_user
        self.edit_question     = edit_question
        self.edit_answer       = edit_answer
        self.edit_test_case    = edit_test_case
        self.edit_permission   = edit_permission
        self.view_student_info = view_student_info
        self.view_teacher_info = view_teacher_info
        self.view_answer       = view_answer
        self.view_test_case    = view_test_case
        self.view_question     = view_question
        self.view_all_question = view_all_question

    @classmethod
    def noID(cls, created, created_by, last_login, username, password, first_name, last_name, role, add_assessment, edit_user, edit_question, edit_answer, edit_test_case, edit_permission, view_student_info, view_teacher_info, view_answer, view_test_case, view_question, view_all_question):
        """
        the parameters correspond with the parameters in the constructor above

        returns a new user with the id parameter set as None and the other
        parameters as they are passed in

        this function acts as a second constructor where you have created a
        user that has not yet been assigned an id from the database
        """
        return cls(None, created, created_by, last_login, username, password, first_name, last_name, role, add_assessment, edit_user, edit_question, edit_answer, edit_test_case, edit_permission, view_student_info, view_teacher_info, view_answer, view_test_case, view_question, view_all_question)

    def __eq__(self, other):
        """
        self  - the user in question
        other - another user that you are comparing 'self' to

        returns a boolean telling if the attributes of 'self'
        and 'other' are the same

        this function overrides the way python compares two users
        and decides if they are equal instead of checking if they
        are the exact same object
        """
        return (
        self.id                == other.id                 and
        self.created           == other.created            and
        self.created_by        == other.created_by         and
        self.last_login        == other.last_login         and
        self.username          == other.username           and
        self.password          == other.password           and
        self.first_name        == other.first_name         and
        self.last_name         == other.last_name          and
        self.role              == other.role               and
        self.add_assessment    == other.add_assessment     and
        self.edit_user         == other.edit_user          and
        self.edit_question     == other.edit_question      and
        self.edit_answer       == other.edit_answer        and
        self.edit_test_case    == other.edit_test_case     and
        self.edit_permission   == other.edit_permission    and
        self.view_student_info == other.view_student_info  and
        self.view_teacher_info == other.view_teacher_info  and
        self.view_answer       == other.view_answer        and
        self.view_test_case    == other.view_test_case     and
        self.view_question     == other.view_question      and
        self.view_all_question == other.view_all_question)

    def setID(self, id):
        """
        self - the user in question
        id   - the id for the user from the database

        this function allows you to assign an id to the user after
        inserting it into the database
        """
        self.id = id

    def __str__(self):
        """
        self - the user in question

        returns a string that fully describes the user 'self'

        this function allows you to convert the user object into
        a human-readable string for viewing the information in it
        """
        string = ""
        string += "id: "                   +      str(self.id)                 + "\n"
        string += "created: "              +      str(self.created)            + "\n"
        string += "created by: "           +      str(self.created_by)         + "\n"
        string += "last login: "           +      str(self.last_login)         + "\n"
        string += "username: "             +          self.username            + "\n"
        string += "password: "             +          self.password            + "\n"
        string += "first name: "           +          self.first_name          + "\n"
        string += "last name: "            +          self.last_name           + "\n"
        string += "role: "                 +          self.role                + "\n"
        string += "permissions:\n"
        string += "\tadd assessment: "     + str(bool(self.add_assessment))    + "\n"
        string += "\tedit user: "          + str(bool(self.edit_user))         + "\n"
        string += "\tedit question: "      + str(bool(self.edit_question))     + "\n"
        string += "\tedit answer: "        + str(bool(self.edit_answer))       + "\n"
        string += "\tedit test case: "     + str(bool(self.edit_test_case))    + "\n"
        string += "\tedit permission: "    + str(bool(self.edit_permission))   + "\n"
        string += "\tview student info: "  + str(bool(self.view_student_info)) + "\n"
        string += "\tview teacher info: "  + str(bool(self.view_teacher_info)) + "\n"
        string += "\tview answer: "        + str(bool(self.view_answer))       + "\n"
        string += "\tview test case: "     + str(bool(self.view_test_case))    + "\n"
        string += "\tview question: "      + str(bool(self.view_question))     + "\n"
        string += "\tview all questions: " + str(bool(self.view_all_question)) + "\n"
        return string
    def toJson(self):
        data = [{
        "id"                :     self.id,
        "created"           : str(self.created),
        "created by"        :     self.created_by,
        "last login"        : str(self.last_login),
        "username"          :     self.username,
        "password"          :     self.password,
        "first name"        :     self.first_name,
        "last name"         :     self.last_name,
        "role"              :     self.role,
        "add assessment"    :     self.add_assessment,
        "edit user"         :     self.edit_user,
        "edit question"     :     self.edit_question,
        "edit answer"       :     self.edit_answer,
        "edit test case"    :     self.edit_test_case,
        "edit permission"   :     self.edit_permission,
        "view student info" :     self.view_student_info,
        "view teacher info" :     self.view_teacher_info,
        "view answer"       :     self.view_answer,
        "view test case"    :     self.view_test_case,
        "view question"     :     self.view_question,
        "view all question" :     self.view_all_question
        }]
        return json.dumps(data)
