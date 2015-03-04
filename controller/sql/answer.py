#!/usr/bin/python3

"""
created_by:         Ebube Chuba
created_date:       3/2/2015
last_modified_by:   Micah Halter
last_modified date: 3/4/2015
"""

# imports
import constants
import json
import mysql.connector
from user import User
from question import Question
from mysql_connect_config import getConfig
# classes
class Answer(object):
    'Answer object to hold attributes and functions for a answer'

    def __init__(self, id, created, created_by, question, score, content, solution, active):
        """
        self       - the answer in answer
        id         - the id number of the answer 'self' in the database
        created    - the date when the answer 'self' was created
        created_by - the user that created the answer 'self'
        question   - the id number of the question the answer 'self' belongs to
        score      - the score of the answer
        content    - the content of hte answer
        solution   - bit defining whether or not an answer is a solution
        active     - bit defining whether or not an answer is active

        this function acts as the constructor to define a new answer object
        """
        self.id         = id
        self.created    = created
        self.created_by = created_by
        self.question   = question
        self.score      = score
        self.content    = content
        self.solution   = solution
        self.active     = active

    def add(self):
        cnx = mysql.connector.connect(**getConfig())
        cursor = cnx.cursor()

        if self.id is None:
            insert = ("INSERT INTO answer (id, created, created_by, question_id, score, content, solution, active) VALUES (%s, '%s', %s, %s, %s, '%s', %s, %s); SELECT LAST_INSET_ID();" % (self.id, self.created, self.created_by.id, self.question.id, self.score, self.content, self.solution, self.active))
            cursor.execute(insert)
            for (id) in cursor:
                self.id=id

        cnx.commit()
        cursor.close()
        cnx.close

    def update(self):
        cnx = mysql.connector.connect(**getConfig())
        cursor = cnx.cursor()

        if self.id is not None:
            update = ("UPDATE answer SET question_id=%s, score=%s, content='%s', solution=%s, active=%s WHERE id=%s" % (self.question.id, self.score, self.content, self.solution, self.active, self.id))
            cursor.execute(update)

        cnx.commit()
        cursor.close()
        cnx.close()

    def activate(self, bool):
        cnx = mysql.connector.connect(**getConfig())
        cursor = cnx.cursor()

        if self.id is not None:
            self.active = int(bool)
            active = ("UPDATE courses SET active=%s WHERE id=%s;" % (int(bool), self.id))

        cursor.execute(active)
        cnx.commit()
        cursor.close()
        cnx.close()

    @classmethod
    def get(self, search="all", testActive=1):
        cnx = mysql.connector.connect(**getConfig())
        cursor = cnx.cursor()

        query = ""
        if search == "all":
            query = "SELECT * FROM answer;"
        elif type(search) is int:
            query = ("SELECT * FROM answer WHERE id=%s" % (search))
        elif type(search) is Question:
            query = ("SELECT * FROM answer WHERE question_id=%s" % (search.id))
        elif type(search) is User:
            query = ("SELECT * FROM answer WHERE created_by=%s" % (search.id))
        cursor.execute(query)

        query += " AND active=%s" % (testActive)

        returnList = []
        for (id, created, created_by, question_id, score, content, solution, active) in cursor:
            user = User.get(created_by)[0]
            question = Question.get(question_id)[0]
            returnList.append(Answer(id, created, user, question, score, content, solution, active))

        cnx.commit()
        cursor.close()
        cnx.close

        return returnList

    def noID(self, created, created_by, question, score, content, solution, active):
        """
        the parameters correspond with the parameters in the constructor above

        returns a new question with the id parameter set as None and the other
        parameters set as they are passed in

        this function acts as a second constructor where you have created a
        answer that has not yet been assigned an id from the database
        """
        return self(None, created, created_by, question, score, content, solution, active)

    def __eq__(self, other):
        """
        self  - the answer in answer
        other - another answer that you are comparing 'self' to

        return a boolean telling if the attributes of self and 'other'
        are the same

        this function overrides the way python compares two answers
        and decides if they are equal instead of checking if they are the
        exact same object
        """
        return (
        self.id         == other.id         and
        self.created    == other.created    and
        self.created_by == other.created_by and
        self.activate   == other.activate   and
        self.question   == other.question   and
        self.score      == other.score      and
        self.content    == other.content    and
        self.solution   == other.solution   and
        self.active     == other.active
        )

    def setID(self, id):
        """
        self - the answer in answer
        id   - the id for the answer from the database

        this function allows you to assign an id to the answer
        after inserting it into the database
        """
        self.id = id

    def __str__(self):
        """
        self - the answer in answer

        returns a string that fully describes the answer 'self'

        this function allows you to convert the answer object into
        a human-readable string for viewing the information in it
        """
        string  = ""
        string += "id: "          + str(self.id)             + "\n"
        string += "created: "     + str(self.created)        + "\n"
        string += "created by: "  + str(self.created_by)     + "\n"
        string += "activate: "    + str(bool(self.activate)) + "\n"
        string += "solution: "    + str(bool(self.solution)) + "\n"
        string += "question: "    + str(question)            + "\n"
        string += "score: "       + str(score)               + "\n"
        string += "answer text: " + str(content)             + "\n"

        return string
    def toJson(self):
        data = {
        "id"         :     self.id,
        "created"    : str(self.created),
        "created by" :     self.created_by,
        "question"   :     self.question_id,
        "score"      :     self.score,
        "content"    :     self.content
        }
        return json.dumps(data)
