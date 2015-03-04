#!/usr/bin/python3

"""
created_by:         Micah Halter
created_date:       2/28/2015
last_modified_by:   EZ
last_modified date: 3/4/2015
"""

# imports
import constants
import mysql.connector
from mysql_connect_config import getConfig

# classes
class Question:
    'Question object to hold attributes and functions for a question'

    def __init__(self, id, created, created_by, language, atype, difficulty, prev_question_id, version_number, last_given, content, topic_list):
        """
        self             - the question in question
        id               - the id number of the question 'self' in the database
        created          - the date when the question 'self' was created
        created_by       - the user that created the question 'self'
        language         - the programming language that the question 'self' was written for
        atype             - the type of question 'self' is
        difficulty       - the difficulty of the question 'self'
        prev_question_id - the id number of a previous version of the question 'self'
        version_number   - the current version number of the question 'self'
        last_given       - the date that the question 'self' was last given
        content          - the content of the question 'self'
        topic_list       - a list of topics that apply to the question 'self'

        this function acts as the constructor to define a new question object
        """
        self.id               = id
        self.created          = created
        self.created_by       = created_by
        self.language         = language
        self.atype            = atype
        self.difficulty       = difficulty
        self.prev_question_id = prev_question_id
        self.version_number   = version_number
        self.last_given       = last_given
        self.content          = content
        self.topic_list       = topic_list

    def noID(cls, created, created_by, language, atype, difficulty, prev_question_id, version_number, last_given, content, topic_list):
        """
        the parameters correspond with the parameters in the constructor above

        returns a new question with the id parameter set as None and the other
        parameters set as they are passed in

        this function acts as a second constructor where you have created a
        question that has not yet been assigned an id from the database
        """
        return cls(None, created, created_by, language, atype, difficulty, prev_question_id, version_number, last_given, content, topic_list)

    def __eq__(self, other):
        """
        self  - the question in question
        other - another question that you are comparing 'self' to

        return a boolean telling if the attributes of self and 'other'
        are the same

        this function overrides the way python compares two questions
        and decides if they are equal instead of checking if they are the
        exact same object
        """
        return (
        self.id               == other.id               and
        self.created          == other.created          and
        self.created_by       == other.created_by       and
        self.language         == other.language         and
        self.atype            == other.atype             and
        self.difficulty       == other.difficulty       and
        self.prev_question_id == other.prev_question_id and
        self.version_number   == other.version_number   and
        self.last_given       == other.last_given       and
        self.content          == other.content          and
        self.topic_list       == other.topic_list)

    def setID(self, id):
        """
        self - the question in question
        id   - the id for the question from the database

        this function allows you to assign an id to the question
        after inserting it into the database
        """
        self.id = id

    def __str__(self):
        """
        self - the question in question

        returns a string that fully describes the question 'self'

        this function allows you to convert the question object into
        a human-readable string for viewing the information in it
        """
        string = ""
        string += "id: "                   + str(self.id)               + "\n"
        string += "created: "              + str(self.created)          + "\n"
        string += "created by: "           + str(self.created_by)       + "\n"
        string += "language: "             +     self.language          + "\n"
        string += "type: "                 +     self.atype              + "\n"
        string += "difficulty: "           + str(self.difficulty)       + "\n"
        string += "previous question id: " + str(self.prev_question_id) + "\n"
        string += "version number: "       + str(self.version_number)   + "\n"
        string += "last given: "           + str(self.last_given)       + "\n"
        string += "content: "              +     self.content           + "\n"

        string += "\nTopics:\n"
        for i in self.topic_list:
            string += "\t" + i.name + "\n"

        return string

    def add(self):

        if self.id is None:
            cnx = mysql.connector.connect(**getConfig())
            cursor = cnx.cursor()

            insert = ("INSERT INTO question (created, created_by, language, type, difficulty, prev_question_id, version_number, last_given, content, active) VALUES (%s, '%s', %s, '%s', '%s', '%s', %s, %s, '%s', '%s', %s); SELECT LAST_INSERT_ID();" % (self.created, self.created_by.id, self.language, self.atype, self.difficulty, self.prev_question_id, self.versioin_number, self.last_given, self.content, self.active))
            cursor.execute(insert)
            for (id) in cursor:
                self.id=id

        cnx.commit()
        cursor.close()
        cnx.close()

    @classmethod
    def get(self, id=0, search="all", testActive=1):
        cnx = mysql.connector.connect(**getConfig())
        cursor = cnx.cursor()

        returnList = []
        query = ""

        if id is 0 and search is "all":
            query = "SELECT * FROM question WHERE"
        if id is not 0:
            query = "SELECT * FROM question WHERE id=%s" % (id)
        if type(search) is User:
            query = "SELECT * FROM question WHERE created_by=%s" % (search.id)
        if type(search) is str:
            query = "SELECT * FROM question WHERE (language='%s' OR type='%s')" % (search, search)
        if type(search) is int:
            query = "SELECT * FROM question WHERE difficulty=%s" % (search)
        if type(search) is Answer:
            query = ("SELECT q.* FROM answer AS a "
                     "INNER JOIN question AS q ON a.question_id=q.id "
                     "WHERE a.question_id=%s" % (search.id))
        if type(search) is Test_Case:
            query = ("SELECT q.* FROM test_case AS t "
                     "INNER JOIN question AS q ON t.question_id=q.id "
                     "WHERE t.question_id=%s" % (search.id))
        if type(search) is Topic:
            query = ("SELECT q.* FROM question_topic AS qt "
                     "INNER JOIN question AS q ON qt.question_id=q.id "
                     "WHERE qt.topic_id=%s" % (search.id))
        if type(search) is Assessment:
            query = ("SELECT q.* FROM assessment_question AS aq "
                     "INNER JOIN question AS q ON aq.question_id=q.id "
                     "WHERE aq.assessment_id=%s" % (search.id))
        query += (" WHERE active=%s;" if id is 0 and search is "all" else " AND active=%s;" % (testActive))

        cursor.execute(query)
        for (id, created, created_by, language, atype, difficulty, prev_question_id, version_number, last_given, content, active) in cursor:
            user = User.get(created_by)[0]
            newQuestion = Question(id, created, user, language, atype, difficulty, prev_question_id, version_number, last_given, content, active)
            returnList.append(newJob)
        cnx.commit()
        cursor.close()
        cnx.close()

    def update(self):
        cnx = mysql.connector.connect(**getConfig())
        cursor = cnx.cursor()

        if self.id is not None:
            update = ("UPDATE question language = '%s', type ='%s', difficulty = '%s', prev_question_id = %s, version_number = %s, last_given = '%s', content = '%s' WHERE id=%s;" % (self.language, self.atype, self. difficulty, self.prev_question_id, self.version_number, self.last_given, self.content, self.id))
            cursor.execute(update)

        cnx.commit()
        cursor.close()
        cnx.close()

    def activate(self, bool):
        cnx = mysql.connector.connect(**getConfig())
        cursor = cnx.cursor()

        if self.active is not None:
            self.active = int(bool)
            active = ("UPDATE question SET active=%s WHERE id=%s;" % (int(bool), self.id))
            cursor.execute(active)

        cnx.commit()
        cursor.close()
        cnx.close()

    def toJson(self):
        data = {
        "id"            : self.id,
        "created"       : self.created,
        "created by"        : self.created_by,
        "language"      : self.language,
        "type"          : self.atype,
        "difficulty"        : self.difficulty,
        "previous question id"  : self.prev_question_id,
        "version number"    : self.version_number,
        "last given"        : self.last_given,
        "content"       : self.content,
        "topics"        : self.topic_list
        }
        return json.dumps(data)
