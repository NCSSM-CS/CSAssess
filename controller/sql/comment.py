#!/usr/local/bin/python3

"""
created_by:         John Fang
created_date:       3/2/2015
last_modified_by:   LZ
last_modified date: 3/5/2015
"""

# imports
import constants
import json
import mysql.connector
from sql.user import User
from sql.answer import Answer
from sql.mysql_connect_config import getConfig
# classes
class Comment(object):
    'Comment object to hold attributes and functions for an assessment'

    def __init__(self, id, created, created_by, answer, content, active):
        """
        self       - the comment in question
        id         - the id number of the comment 'self' in the database
        created    - the date when the comment 'self' was created
        created_by - the user that created the comment 'self'
        answer     - the answer of the comment 'self'
        content    - the content of the topic 'self'

        this function acts as the constructor to define a new topic object
        """
        self.id         = id
        self.created    = created
        self.created_by = created_by
        self.answer     = answer
        self.content    = content
        self.active     = active

    def add(self):

        if self.id is not None:
            return

        cnx = mysql.connector.connect(**getConfig())
        cursor = cnx.cursor()

        insert = ("INSERT INTO comment (created_by, answer_id, content, active) VALUES (%s, '%s', '%s', %s);" %(self.created_by.id, self.answer.id, self.content, self.active))
        cursor.execute(insert)

        select = "SELECT LAST_INSERT_ID();"

        cursor.execute(select)

        for (id) in cursor:
            self.id=id

        cnx.commit()
        cursor.close()
        cnx.close()

    def update(self):

        cnx = mysql.connector.connect(**getConfig())
        cursor = cnx.cursor()

        if self.id is not None:
            update = ("UPDATE comment SET answer_id = %s,  content = '%s', active = %s WHERE id = %s;" % (self.answer.id, self.content, self.active, self.id))
            cursor.execute(update)

        cnx.commit()
        cursor.close()
        cnx.close()

    def activate(self, bool):
        cnx = mysql.connector.connect(**getConfig())
        cursor = cnx.cursor()

        if self.id is not None:
            self.active = int(bool)
            update = ("UPDATE comment SET active=%s WHERE id=%s;" % (int(bool), self.id))
            cursor.execute(update)

        cnx.commit()
        cursor.close()
        cnx.close()

    @classmethod
    def get(self, search="all", testActive=1):
        cnx = mysql.connector.connect(**getcConfig())
        cursor = cnx.cursor()

        returnList = []
        query = ""
        if search == "all":
            query = "SELECT * FROM comment"
        elif type(search) is int:
            query = ("SELECT * FROM comment WHERE id=%s" % (search))
        elif str(type(search)) is "<class 'sql.user.User'>":
            query = ("SELECT * FROM comment WHERE created_by=%s" % (search.id))
        elif str(type(search)) is "<class 'sql.answer.Answer'>":
            query = ("SELECT * FROM comment WHERE answer_id=%s" % (search.id))

        query += (" WHERE active=%s;" if search == "all" else " AND active =%s;") % (testActive)
        cursor.execute(query)
        for (id, created, created_by, answer_id, content, active) in cursor:
            user = User.get(created_by)[0]
            answer = Answer.get(answer_id)[0]
            returnList.append(Comment(id, created, user, answer, content, active))

        cnx.commit()
        cursor.close()
        cnx.close

        return returnList

    def noID(self, created, created_by, answer, content, active):
        """
        the parameters correspond with the parameters in the constructor above

        returns a new comment with the id parameter set as None and the other
        parameters as they are passed in

        this function acts as a second constructor where you have created a
        comment that has not yet been assigned an id from the database
        """
        return self(None, None, created_by, answer, content, active)

    def __eq__(self, other):
        """
        self  - the comment in question
        other - other comment that you are comparing 'self' to

        returns a boolean telling if the attributes of 'self'
        and 'other' are the same

        this function overrides the way python compares two comments
        and decides if they are equal instead of checking if they
        are the exact same object
        """
        return (
        self.id         == other.id         and
        self.created    == other.created    and
        self.created_by == other.created_by and
        self.answer     == other.answer     and
        self.content    == other.content    and
        self.active     == other.active
        ) if type(other) is Comment else False

    def __str__(self):
        """
        self - the comment in question

        returns a string that fully describes the comment 'self'

        this function allows you to convert the comment object into
        a human-readable string for viewing the information in it
        """
        string = ""
        string += "id: "         +      str(self.id)         + "\n"
        string += "created: "    +      str(self.created)    + "\n"
        string += "created by: " +      str(self.created_by) + "\n"
        string += "active: "     + str(bool(self.active))    + "\n"
        string += "answer: "     +      str(self.answer)     + "\n"
        string += "content: "    +          self.content     + "\n"

        return string

    def toJson(self):
        data = {
        "id"        : self.id,
        "created"   : self.created,
        "createdBy": self.created_by,
        "active"    : self.active,
        "answer"    : self.answer,
        "content"   : self.content
        }
        return json.dumps(data)
