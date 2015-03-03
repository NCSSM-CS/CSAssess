#!/usr/bin/python

"""
created_by:         Micah Halter
created_date:       3/1/2015
last_modified_by:   EZ
last_modified date: 3/3/2015
"""

# imports
import constants
import json

# classes
class Section:
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
    def noID(cls, created, created_by, course, year, term, period, active):
        """
        the parameters correspond with the parameters in the constructor above

        returns a new section with the id parameter set as None and the other
        parameters as they are passed in

        this function acts as a second constructor where you have created an
        assessment that has not yet been assigned an id from the database
        """
        return cls(None, created, created_by, course, year, term, period, active)

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
        string += "course: "   + str(self.course)     + "\n"
        string += "year: "       + str(self.year)       + "\n"
        string += "term: "       +     self.term        + "\n"
        string += "period: "     +     self.period      + "\n"
	string += "active: "     + str(self.active)     + "\n"

        return string

    def add(self):

	if self.id is not None:
	    return

	cnx = mysql.connector.connect(**getConfig())
        cursor = cnx.cursor()

	insert = ("INSERT INTO section (id, created, created_by, course, year, term, period, active) VALUES (%s, '%s', %s, %s, %s, '%s', '%s', %s); SELECT LAST_INSERT_ID();" % (self.id, self.created, self.created_by.id, self.course.id, self.year, self.term, self.period, self.active))

	cursor.execute(insert)

	for(id) in cursor:
	    self.id=id

        cnx.commit()
        cursor.close()
        cnx.close()

    def update(self):
        cnx = mysql.connector.connect(**getConfig())
	cursor = cnx.cursor()

	if self.id is not None:
	    update = ("UPDATE job SET created = '%s', created_by = %s, course = %s, year = %s, term = '%s', period = '%s', active = %s;" % (self.created, self.created_by.id, self.course.id, self.year, self.term, self.period, self.active))

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
    def get(self, search, active):
        pass

    def toJson(self):
        data = [{
        "id"            :     self.id,
        "created"       : str(self.created),
        "created by"    :     self.created_by,
        "course"        :     self.course,
        "year"          :     self.year,
        "term"          :     self.term,
        "period"        :     self.period
        }]
        return json.dumps(data)
