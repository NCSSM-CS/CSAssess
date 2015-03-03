#!/usr/bin/python

"""
created_by:         Micah Halter
created_date:       3/1/2015
last_modified_by:   EZ
last_modified date: 3/2/2015
"""

# imports
import constants
import json
import mysql.connector
from user import User
from mysql_connect_config import getConfig

# classes
class Course:
    'Course object to hold attributes and functions for a course'

    def __init__(self, id, created, created_by, course_code, name, active):
        """
        self        - the course in question
        id          - the id number of the course 'self' in the database
        created     - the date when the course 'self' was created
        created_by  - the user that created the course 'self'
        course_code - the course code of the course 'self'
        name        - the name of the course 'self'
        """
        self.id          = id
        self.created     = created
        self.created_by  = created_by
        self.course_code = course_code
        self.name        = name
        self.active      = active

    @classmethod
    def noID(self, created, created_by, course_code, name, active):
        """
        the parameters correspond with the parameters in the constructor above

        returns a new course with the id parameter set as None and the other
        parameters as they are passed in through parameters

        this function acts as a second constructor where you have created a
        course that has not yet been assigned an id from the database
        """
        return self(None, created, created_by, course_code, name, active)

    def __eq__(self, other):
        """
        self  - the course in question
        other - another course that you are comparing 'self' to

        returns a boolean telling if the attributes of 'self'
        and 'other' are the same

        this function overrides the way python compares two courses
        and decides if they are equal instead of checking if they
        are the exact same object
        """
        return (
        self.id          == other.id          and
        self.created     == other.created     and
        self.created_by  == other.created_by  and
        self.course_code == other.course_code and
        self.name        == other.name        and
        self.active      == other.active)

    def __str__(self):
        """
        self - the course in question

        returns a string that fully describes the course 'self'

        this functions allows you to convert the course object
        into a human-readable string for viewing the information
        in it
        """
        string = ""
        string += "id: "          +      str(self.id)                   + "\n"
        string += "created: "     +      str(self.created)              + "\n"
        string += "created by: "  +      str(self.created_by.username)  + "\n"
        string += "active: "      + str(bool(self.active))              + "\n"
        string += "course code: " +      str(self.course_code)          + "\n"
        string += "name: "        +          self.name                  + "\n"

        return string

    def add(self):

	if self.id is not None:
		return

    	cnx = mysql.connector.connect(**getConfig())
	cursor = cnx.cursor()

	insert = ("INSERT INTO courses (id, created, created_by, type, section_id, name, active) VALUES (%s, '%s', %s,'%s', %s, '%s', %s); SELECT LAST_INSERT_ID();" % (self.id, self.created, self.created_by, self.type, self.section_id, self.name, self.active))
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
                update = ("UPDATE courses SET created = '%s', created_by = %s, type = '%s',, section_id = %s, name = '%s' WHERE id = %s;" % (self.created, self.created_by, self.type, self.section_id, self.name, self.id))
	        cursor.execute(update)

	cnx.commit()
	cursor.close()
	cnx.close()

    def activate(self, bool):
    	cnx = mysql.connector.connect(**getConfig())
	cursor = cnx.cursor()

        self.active = int(bool)
	active = ("UPDATE course SET active=%s WHERE id=%s;" % (int(bool), self.id))

	cursor.execute(active)

	cnx.commit()
	cursor.close()
	cnx.close()


    @classmethod
    def get(self, id="all", testActive=1):
        cnx = mysql.connector.connect(**getConfig())
        cursor = cnx.cursor()

        returnList = []
        query = ""
        if id == "all":
            query = "SELECT * FROM course"
        else:
            query = ("SELECT * FROM course WHERE id=%s" % (id))

        query += " AND active=%s;" % (testActive)
        cursor.execute(query)
        for (id, created, created_by, course_code, name, active) in cursor:
            user = User.get(created_by)[0]
            returnList.append(Course(id, created, user, course_code, name, active))

        cnx.commit()
        cursor.close()
        cnx.close()

        return returnList

    def toJson(self):
        data = [{
        "id"            :     self.id,
        "created"       : str(self.created),
        "cread_by"      :     self.created_by,
        "course_code"   :     self.course_code,
        "name"          :     self.name
        }]
        return json.dumps(data)

