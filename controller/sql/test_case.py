#!/usr/local/bin/python

"""
created_by:         Keshav Patel
created_date:       3/2/2015
last_modified_by:   LZ
last_modified date: 3/5/2015
"""

# imports
import constants
from question import Question

# classes
class Test_Case(object):
    'test_case object to hold attributes and functions for a test_case'

    def __init__(self, id, created, created_by, question, weight, content, active):
        """
        self          - the test_case in question
        id            - the id number of the test_case 'self' in the database
        created       - the date when the test_case 'self' was created
        created_by    - the user that created the test_case 'self'
        question      - the question associated with 'self'
        weight        - the weight given to this test_case
        content       - the code for this test_case
        active        - a bit telling whether the test_case is active

        this function acts as the constructor to define a new test_case object
        """
        self.id          = id
        self.created     = created
        self.created_by  = created_by
        self.question    = question
        self.weight      = weight
        self.content     = content
        self.active      = active

    @classmethod
    def noID(self, created, created_by, question, weight, content, active):
        """
        the parameters correspond with the parameters in the constructor above

        returns a new test_case with the id parameter set as None and the other
        parameters as they are passed in

        this function acts as a second constructor where you have created a
        test_case that has not yet been assigned an id from the database
        """
        return self(self, created, created_by, question, weight, content, active)

    def __eq__(self, other):
        """
        self  - the test_case in question
        other - another test_case that you are comparing 'self' to

        returns a boolean telling if the attributes of 'self' and 'other'
        are the same

        this function overrides the way python compares two assignments
        and decides if they are equal instead of checking if they are the
        exact same object
        """
        return (
        self.id          == other.id          and
        self.created     == other.created     and
        self.created_by  == other.created_by  and
        self.question    == other.question    and
        self.weight      == other.weight      and
        self.content     == other.content     and
        self.active      == self.active)

    def __str__(self):
        """
        self - the test_case in question

        returns a string that fully describes the test_case 'self'

        this function allows you to convert the test_case object into
        a human-readable string for viewing the information in it
        """
        string  = ""
        string += "id: "         + str(self.id)           + "\n"
        string += "created: "    + str(self.created)      + "\n"
        string += "created by: " + str(self.created_by)   + "\n"
        string += "active: "     + str(bool(self.active)) + "\n"
        string += "question "    + str(self.question)     + "\n"
        string += "weight "      + str(self.weight)       + "\n"
        string += "content "     + self.content           + "\n"
        return string

    def add(self):
        cnx = mysql.connector.connect(**getConfig())
        cursor = cnx.cursor()

        if self.id is None:
            insert = ("INSERT INTO test_case (created_by, question_id, weight, content, active) VALUES (%s, %s, %s, '%s', %s);" % (self.created_by.id, self.question.id, self.weight, self.content, self.active))
            cursor.execute(insert)

            select = "SELECT LAST_INSERT_ID();"

            cursor.execute(select)

            for (id) in cursor:
                self.id = id

        cnx.commit()
        cursor.close()
        cnx.close()

    @classmethod
    def get(self, search="all", testActive=1):
        returnList = []
        query = ""
        if search == "all":
            query = "SELECT * FROM test_cases"
        elif type(search) is int:
            query = "SELECT * FROM test_cases WHERE id=%s" % (search)
        elif type(search) is User:
            query = "SELECT * FROM test_cases WHERE created_by=%s" % (search.id)
        elif type(search) is Question:
            query = "SELECT * FROM test_cases WHERE question_id=%s" % (search.id)
        query += (" WHERE active=%s;" if search=="all" else " AND active=%s;") % (testActive)

        cursor.execute(query)
        for (id, created, created_by, question_id, weight, content, active) in cursor:
            user = User.get(created_by)[0]
            question = Question.get(question_id)[0]
            returnList.append(Test_Case(id, created, user, question, weight, content, active))

        return returnList

    def update(self):
        cnx = mysql.connector.connect(**getConfig())
        cursor = cnx.cursor()

        if self.id is not None:
            update = "UPDATE test_case SET question_id=%s, weight=%s, content='%s', active=%s WHERE id=%s;" % (self.question.id, self.weight, self.content, self.active, self.id)
            cursor.execute(update)

        cnx.commit()
        cursor.close()
        cnx.close()

    def activate(self, bool):
        cnx = mysql.connector.connect(**getConfig())
        cursor = cnx.cursor()

        if self.id is not None:
            update = "UPDATE test_case SET active=%s WHERE id=%s;" % (int(bool), self.id)
            cursor.execute(update)

        cnx.commit()
        cursor.close()
        cnx.close()

    def toJson(self):
        data = {
                "id"         : self.id,
                "created"    : self.created,
                "createdBy" : self.created_by,
                "question"   : self.question,
                "weight"     : self.weight,
                "content"    : self.content,
                "active"     : self.active,
                }
        return json.dumps(data)
