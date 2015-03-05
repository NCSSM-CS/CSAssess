#!/usr/local/bin/python3

"""
created_by:         Micah Halter
created_date:       3/1/2015
last_modified_by:   Micah Halter
last_modified date: 3/4/2015
"""

# imports
import constants
from user import User
from course import Course
import json
import mysql.connector
from mysql_connect_config import getConfig

# classes
class Section(object):
    'Section object to hold attributes and functions for a section'

    def __init__(self, id, created, created_by, course, year, term, period, active):
        """
        self       - the section in question
        id         - the id number of the section 'self' in the database
        created    - the date when the section 'self' was created
        created_by - the user that created the section 'self'
        course     - the course that the section 'self' is in
        year       - the year that the section 'self' took place in
        term       - the term that the section 'self' took place in
        period     - the period that the section 'self' took place in
        active     - bit specifying whether job is active or inactive

        this function acts as the constructor to define a new section object
        """
        self.id         = id
        self.created    = created
        self.created_by = created_by
        self.course     = course
        self.year       = year
        self.term       = term
        self.period     = period
        self.active     = active

    @classmethod
    def noID(self, created, created_by, course, year, term, period, active):
        """
        the parameters correspond with the parameters in the constructor above

        returns a new section with the id parameter set as None and the other
        parameters as they are passed in

        this function acts as a second constructor where you have created an
        assessment that has not yet been assigned an id from the database
        """
        return self(None, created, created_by, course, year, term, period, active)

    def __eq__(self, other):
        """
        self  - the section in question
        other - another section that you are comparing 'self' to

        returns a boolean telling if the attributes of 'self' and 'other'
        are the same

        this function overrides the way python compares two sections
        and decides if they are equal instead of checking if they are
        the exact same object
        """
        return (
        self.id         == other.id         and
        self.created    == other.created    and
        self.created_by == other.created_by and
        self.course     == other.course     and
        self.year       == other.year       and
        self.term       == other.term       and
        self.period     == other.period     and
        self.active     == other.active)

    def __str__(self):
        """
        self - the section in question

        returns a string that fully describes the section 'self'

        this function allows you to convert the section object into
        a human-readable string for viewing the information in it
        """
        string = ""
        string += "id: "         + str(self.id)         + "\n"
        string += "created: "    + str(self.created)    + "\n"
        string += "created by: " + str(self.created_by) + "\n"
        string += "active: "     + str(self.active)     + "\n"
        string += "course: "   + str(self.course)     + "\n"
        string += "year: "       + str(self.year)       + "\n"
        string += "term: "       +     self.term        + "\n"
        string += "period: "     +     self.period      + "\n"

        return string

    def add(self):
        cnx = mysql.connector.connect(**getConfig())
        cursor = cnx.cursor()

        if self.id is None:
            insert = ("INSERT INTO section (created_by, course, year, term, period, active) VALUES (%s, '%s', %s, %s, %s, '%s', '%s', %s);" % (self.created_by.id, self.course.id, self.year, self.term, self.period, self.active))
            cursor.execute(insert)

            select = "SELECT LAST_INSERT_ID();"
            cursor.execute(select)


            for(id) in cursor:
                self.id=id

        cnx.commit()
        cursor.close()
        cnx.close()

    def update(self):
        cnx = mysql.connector.connect(**getConfig())
        cursor = cnx.cursor()

        if self.id is not None:
            update = ("UPDATE job SET course = %s, year = %s, term = '%s', period = '%s', active = %s;" % (self.course.id, self.year, self.term, self.period, self.active))

            cursor.execute(update)

        cnx.commit()
        cursor.close()
        cnx.close()

    def activate(self, bool):
        cnx = mysql.connector.connect(**getConfig())
        cursor = cnx.cursor()

        if self.active is not None:

            self.active = int(bool)
            active = ("UPDATE section SET active=%s WHERE id=%s;" % (int(bool), self.id))

            cursor.execute()

        cnx.commit()
        cursor.close()
        cnx.close()

    @classmethod
    def get(self, search="all", searchYear=None, searchTerm=None, searchUser=None, testActive="1"):
        """

        """
        cnx = mysql.connector.connect(**getConfig())
        cursor = cnx.cursor()

        returnList = []
        query = ""
        if search == "all" and searchYear is None and searchTerm is None and searchUser is None:
            query = "SELECT * FROM section"
        elif searchYear is not None:
            query = ("SELECT * FROM section WHERE year = %s" % (searchYear))
        elif searchTerm is not None:
            query = ("SELECT * FROM section WHERE term = '%s'" % (searchTerm))
        elif searchUser is not None:
            query = ("SELECT s.* FROM section_user AS su "
                     "INNER JOIN section AS s ON su.section_id=s.id "
                     "WHERE su.user_id=%s" % (search.id))
        elif type(search) is int:
            query = ("SELECT * FROM section WHERE id = %s" % (search))
        elif type(search) is user:
            query = ("SELECT * FROM section WHERE created_by = %s" % (search.id))
        elif type(search) is course:
            query = ("SELECT * FROM section WHERE course_id = %s" % (search.id))
        elif type(search) is str:
            query = ("SELECT * FROM section WHERE period = '%s'" % (search))
        query += (" WHERE active = %s;" if search == "all" else " AND active = %s;") % (testActive)
        cursor.execute(query)

        for(id, created, created_by, course_id, year, term, period, active) in cursor:

            user = User.get(created_by)[0]
            course = Course.get(course_id)[0]
            returnList.append(Section(id, created, user, course, year, term, period, active))

        cnx.commit()
        cursor.close()
        cnx.close()

        return returnList

    def toJson(self):
        data = {
        "id"            :     self.id,
        "created"       : str(self.created),
        "created by"    :     self.created_by,
        "active"        :     self.active,
        "course"        :     self.course,
        "year"          :     self.year,
        "term"          :     self.term,
        "period"        :     self.period
        }
        return json.dumps(data)
