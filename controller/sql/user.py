#!/usr/local/bin/python3

"""
created_by:         Micah Halter
created_date:       3/1/2015
last_modified_by:   LZ
last_modified date: 3/5/2015
"""

# imports
import constants
import json
import mysql.connector
from mysql_connect_config import getConfig

# classes
class User(object):
    'Assessment object to hold attributes and functions for an assessment'

    def __init__(self, id, created, created_by, last_login, username, password, first_name, last_name, role, add_assessment, edit_user, edit_question, edit_answer, edit_test_case, edit_permission, view_student_info, view_teacher_info, view_answer, view_test_case, view_question, view_all_question, active):
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
        active            - whether the user is an active user or not

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
        self.active            = active

    @classmethod
    def noID(self, created, created_by, last_login, username, password, first_name, last_name, role, add_assessment, edit_user, edit_question, edit_answer, edit_test_case, edit_permission, view_student_info, view_teacher_info, view_answer, view_test_case, view_question, view_all_question, active):
        """
        the parameters correspond with the parameters in the constructor above

        returns a new user with the id parameter set as None and the other
        parameters as they are passed in

        this function acts as a second constructor where you have created a
        user that has not yet been assigned an id from the database
        """
        return self(None, created, created_by, last_login, username, password, first_name, last_name, role, add_assessment, edit_user, edit_question, edit_answer, edit_test_case, edit_permission, view_student_info, view_teacher_info, view_answer, view_test_case, view_question, view_all_question, active)

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
        self.view_all_question == other.view_all_question  and
        self.active            == other.active
        ) if type(other) is User else False

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
        string += "active: "               + str(bool(self.active))            + "\n"
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

    def add(self):
        cnx = mysql.connector.connect(**getConfig())
        cursor = cnx.cursor()

        if self.id is None:
            insert = ("INSERT INTO user (created_by, last_login, username, password, first_name, last_name, role, add_assessment, edit_user, edit_question, edit_answer, edit_test_case, edit_permission, view_student_info, view_teacher_info, view_answer, view_test_case, view_question, view_all_question, active) VALUES ('%s', %s, '%s', '%s', '%s', '%s', '%s', '%s', %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);" % (self.created_by.id, self.last_login, self.username, self.password, self.first_name, self.last_name, self.role, self.add_assessment, self.edit_user, self.edit_question, self.edit_answer, self.edit_test_case, self.edit_permission, self.view_student_info, self.view_teacher_info, self.view_answer, self.view_test_case, self.view_question, self.view_all_question, self.active))
            cursor.execute(insert)

            select = "SELECT LAST_INSERT_ID();"

            cursor.execute(select)

            for (id) in cursor:
                self.id = id

        cnx.commit()
        cursor.close()
        cnx.close()

    @classmethod
    def get(self, search="all", searchUser=None, testActive=1):
        cnx = mysql.connector.connect(**getConfig())
        cursor = cnx.cursor()

        returnList = []
        query = ""
        if search == "all":
            query = "SELECT * FROM user"
        elif search == None and type(searchUser) is str:
            query = "SELECT * FROM user WHERE username=%s" % (searchUser)
        elif type(search) is int:
            query = ("SELECT * FROM user WHERE id=%s" % (search))
        elif type(search) is str:
            query = ("SELECT * FROM user WHERE (first_name LIKE '%s%%' OR last_name LIKE '%s%%')" % (search, search))
        elif str(type(search)) == "<class 'section.Section'>":
            query = ("SELECT * FROM user WHERE section_id='%s'" % (search.id))
        elif str(type(search)) == "<class 'assessment.Assessment'>":
            query = ("SELECT u.* FROM user_assessment AS ua "
                     "INNER JOIN user AS u ON ua.user_id=u.id "
                     "WHERE ua.assessment_id=%s"
                     % (search.id))

        query += (" WHERE active=%s;" if search=="all" else " AND active=%s;") % (testActive)


        cursor.execute(query)
        for (id, created, created_by, last_login, username, password, first_name, last_name, role, add_assessment, edit_user, edit_question, edit_answer, edit_test_case, edit_permission, view_student_info, view_teacher_info, view_answer, view_test_case, view_question, view_all_question, active) in cursor:
            user = username if created_by == id else User.get(created_by)
            returnList.append(User(id, created, user, last_login, username, password, first_name, last_name, role, add_assessment, edit_user, edit_question, edit_answer, edit_test_case, edit_permission, view_student_info, view_teacher_info, view_answer, view_test_case, view_question, view_all_question, active))

        """
        WARNING: Potential bug if username (str) is passed: If user==username and string is passed, then attempting to pull user.id from this object will throw an error. No fix currently known, hopefully no one will attempt to return the god user in a search made by god user?
        """

        cnx.commit()
        cursor.close()
        cnx.close()

        return returnList

    def update(self):
        cnx = mysql.connector.connect(**getConfig())
        cursor = cnx.cursor()

        if self.id is not None:
            update = ("UPDATE user SET last_login='%s', username='%s', password='%s', first_name='%s', last_name='%s', role='%s', add_assessment=%s, edit_user=%s, edit_question=%s, edit_answer=%s, edit_test_case=%s, edit_permission=%s, view_student_info=%s, view_teacher_info=%s, view_answer=%s, view_test_case=%s, view_question=%s, view_all_question=%s, active=%s WHERE id=%s;" % (self.last_login, self.username, self.password, self.first_name, self.last_name, self.role, self.add_assessment, self.edit_user, self.edit_question, self.edit_answer, self.edit_test_case, self.edit_permission, self.view_student_info, self.view_teacher_info, self.view_answer, self.view_test_case, self.view_question, self.view_all_question, self.active, self.id))
            cursor.execute(update)

        cnx.commit()
        cursor.close()
        cnx.close()

    def activate(self, bool):
        cnx = mysql.connector.connect(**getConfig())
        cursor = cnx.cursor()

        if self.id is not None:
            self.active = int(bool)
            update = ("UPDATE user SET active=%s WHERE id=%s;" % (int(bool), self.id))
            cursor.execute(update)

            cnx.commit()
            cursor.close()
            cnx.close()

    def toJson(self):
        data = {
                "id"                :     self.id,
                "created"           : str(self.created),
                "createdBy"        :     self.created_by,
                "lastLogin"        : str(self.last_login),
                "active"            :     self.active,
                "username"          :     self.username,
                "password"          :     self.password,
                "firstName"        :     self.first_name,
                "lastName"         :     self.last_name,
                "role"              :     self.role,
                "addAssessment"    :     self.add_assessment,
                "editUser"         :     self.edit_user,
                "editQuestion"     :     self.edit_question,
                "editAnswer"       :     self.edit_answer,
                "editTest case"    :     self.edit_test_case,
                "editPermission"   :     self.edit_permission,
                "viewStudent info" :     self.view_student_info,
                "viewTeacher info" :     self.view_teacher_info,
                "viewAnswer"       :     self.view_answer,
                "viewTestCase"    :     self.view_test_case,
                "viewQuestion"     :     self.view_question,
                "viewAllQuestion" :     self.view_all_question
                }
        return json.dumps(data)
