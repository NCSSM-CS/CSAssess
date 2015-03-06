#!/usr/local/bin/python3

"""
created_by:         Micah Halter
created_date:       2/28/2015
last_modified_by:   LZ
last_modified date: 3/5/2015
"""

# imports
import constants
import mysql.connector
from sql.user import User
from sql.mysql_connect_config import getConfig

# classes
class Topic(object):
    'Assessment object to hold attributes and functions for an assessment'

    def __init__(self, id, created, created_by, name, active):
        """
        self       - the topic in question
        id         - the id number of the topic 'self' in the database
        created    - the date when the topic 'self' was created
        created_by - the user that created the topic 'self'
        name       - the name of the topic 'self'
        active     - a bit specifying whether the topic is active

        this function acts as the constructor to define a new topic object
        """
        self.id         = id
        self.created    = created
        self.created_by = created_by
        self.name       = name
        self.active     = active

    @classmethod
    def noID(self, created, created_by, name, active):
        """
        the parameters correspond with the parameters in the constructor above

        returns a new assessment with the id parameter set as None and the other
        parameters as they are passed in

        this function acts as a second constructor where you have created a
        topic that has not yet been assigned an id from the database
        """
        return self(None, created, created_by, name, active)

    @classmethod
    def get(self, search="all", testActive=1):
        cnx = mysql.connector.connect(**getConfig())
        cursor = cnx.cursor()

        returnList = []
        query = ""
        if search == "all":
            query = ("SELECT * FROM topic")
        elif type(search) is int:
            query = ("SELECT * FROM topic WHERE id=%s" % (search))
        elif type(search) is str:
            query = ("SELECT * FROM topic WHERE (name LIKE '%%s%%')" % (search))
        elif str(type(search)) == "<class 'sql.user.User'>":
            query = ("SELECT * FROM topic WHERE created_by=%s" % (search.id))
        elif str(type(search)) == "<class 'sql.question.Question'>":
            query = ("SELECT t.* FROM question_topic AS qt "
                     "INNER JOIN topic AS t ON qt.topic_id=t.id "
                     "WHERE qt.question_id=%s"
                     % (search.id))
        elif str(type(search)) == "<class 'sql.assessment.Assessment'>":
            query = ("SELECT t.* FROM assessment_topic AS at "
                     "INNER JOIN topic AS t ON at.topic_id=t.id "
                     "WHERE at.assessment_id=%s"
                     % (search.id))

        query += (" WHERE active=%s;" if search == "all" else " AND active=%s;") % (testActive)

        cursor.execute(query)
        for (id, created, created_by, name, active) in cursor:
            user = User.get(created_by)[0]
            returnList.append(Topic(id, created, user, name, active))

        cnx.commit()
        cursor.close()
        cnx.close()

        return returnList

    def add(self):
        cnx = mysql.connector.connect(**getConfig())
        cursor = cnx.cursor()

        if self.id is None:
            insert = ("INSERT INTO topic (created_by, name, active) VALUES ('%s', %s, '%s', %s);" % (self.created, self.created_by.id, self.name, self.active))
            cursor.execute(insert)

            select = "SELECT LAST_INSERT_ID();"

            cursor.execute(select)

            for (id) in cursor:
                self.id = id

        cnx.commit()
        cursor.close()
        cnx.close()

    def update(self):
        cnx = mysql.connector.connect(**getConfig())
        cursor = cnx.cursor()

        if self.id is not None:
            update = ("UPDATE topic SET name='%s', active=%s" % (self.name, self.active))
            cursor.execute(update)

        cnx.commit()
        cursor.cloes()
        cnx.close()

    def activate(self, bool):
        cnx = mysql.connector.connect(**getConfig())
        cursor = cnx.cursor()

        if self.id is not None:
            self.active = int(bool)
            update = ("UPDATE topic SET active=%s WHERE id=%s" % (int(bool), self.id))
            cursor.execute(update)

            cnx.commit()
            cursor.close()
            cnx.close()

    def __eq__(self, other):
        """
        self  - the topic in question
        other - other topic that you are comparing 'self' to

        returns a boolean telling if the attributes of 'self'
        and 'other' are the same

        this function overrides the way python compares two topics
        and decides if they are equal instead of checking if they
        are the exact same object
        """
        return (
        self.id         == other.id         and
        self.created    == other.created    and
        self.created_by == other.created_by and
        self.name       == other.name       and
        self.active     == other.active
        ) if type(other) is Topic else False

    def __str__(self):
        """
        self - the topic in question

        returns a string that fully describes the assessment 'self'

        this function allows you to convert the topic object into
        a human-readable string for viewing the information in it
        """
        string = ""
        string += "id: "         +      str(self.id)         + "\n"
        string += "created: "    +      str(self.created)    + "\n"
        string += "created by: " +      str(self.created_by) + "\n"
        string += "active: "     + str(bool(self.active))    + "\n"
        string += "name: "       +          self.name        + "\n"
        string += "active: "       +    str(self.active)     + "\n"

        return string
    def toJson(self):
        data = {
        "id"        : self.id,
        "created"   : self.created,
        "createdBy": self.created_by,
        "name"      : self.name,
        "active"    : self.active
        }
        return json.dumps(data)

