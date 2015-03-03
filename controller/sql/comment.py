#!/usr/bin/python

"""
created_by:         John Fang
created_date:       3/2/2015
last_modified_by:   Matthew Bent (Bear)
last_modified date: 3/3/2015
"""

# imports
import constants
import json
import mysql.connector
from user import User
from mysql_connecto_config import getConfig
# classes
class Comment(object):
    'Comment object to hold attributes and functions for an assessment'

    def __init__(self, id, created, created_by, answer, content):
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
    def add(self):
        
        if self.id is not None:
            return
        
        cnx = mysql.connector.connect(**getConfig())
        cursor = cnx.cursor()

        insert = ("INSERT INTO comment (id, created, created_by, answer_id, content, active) VALUES (%s, '%s', %s, '%s', '%s', %s); SELECT LAST_LAST_INSERT_ID();" %(self.id, self.created, self.created_by.id, self.answer_id, self.content, self.active))
        cursor.execute(insert)

        for (id) in cursor:
            self.id=id

        cnx.commit()
        cursor.close()
        cnx.close()
    
    def edit(self):
        
        cnx = mysql.connector.connect(**getConfig())
        cursor = cnx.cursor()

        if self.id is not None:
            update = ("UPDATE comment SET created = '%s', created_by = %s, answer_id = %s,  content = '%s' WHERE id = %s;" % (self.created, self.created_by.id, self.asnwer_id, self.content, self.id))
            cursor.execute(update)

        cnx.commit()
        cursor.close()
        cnx.close()
        
    def activate(self, bool):
        cnx = mysql.connector.connect(**getConfig())
        cursor = cnx.cursor()

	self.active = int(bool)
        active = ("UPDATE comment SET active=%s WHERE id=%S;" % (int(bool), self.id))

        cursor.execute(active)

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
        elif type(search) is User:
            query = ("SELECT * FROM comment WHERE created_by=%s" % (search))
        elif type(search) is Answer: 
            query = ("SELECT * FROM comment WHERE answer_id=%s" % (search))

        query += " AND active =%s;" % (testActive)
        cursor.execute(query)
        for (id, created, created_by, answer_id, content, active) in cursor:
            user = User.get(created_by)[0]
            newComment = Comment(id, created, user, answer_id, content, active)
            if newComment not in returnList:
                returnList.append(newComment)
        
        cnx.commit()
        cursor.close()
        cnx.close

        return returnList

    def noID(self, created, created_by, answer, content):
        """
        the parameters correspond with the parameters in the constructor above

        returns a new comment with the id parameter set as None and the other
        parameters as they are passed in

        this function acts as a second constructor where you have created a
        comment that has not yet been assigned an id from the database
        """
        return self(None, created, created_by, answer, content)

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
        self.content    == other.content)

    def setID(self, id):
        """
        self - the comment in question
        id   - the id for the comment from the database

        this function allows you to assign an id to the comment
        after inserting it into the database
        """
        self.id = id

    def __str__(self):
        """
        self - the comment in question

        returns a string that fully describes the comment 'self'

        this function allows you to convert the comment object into
        a human-readable string for viewing the information in it
        """
        string = ""
        string += "id: "         + str(self.id)         + "\n"
        string += "created: "    + str(self.created)    + "\n"
        string += "created by: " + str(self.created_by) + "\n"
        string += "answer: "     + str(self.answer)     + "\n"
        string += "content: "    + self.content         + "\n"
        return string
    def toJson(self):
        data = [{
        "id"        : self.id,
        "created"   : self.created,
        "created by": self.created_by,
        "answer"    : self.answer,
        "content"   : self.content
        }]
        return json.dumps(data)
