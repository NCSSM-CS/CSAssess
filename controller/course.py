#!/usr/bin/python

"""
created_by:         Micah Halter
created_date:       3/1/2015
last_modified_by:   Micah Halter
last_modified date: 3/1/2015
"""

# imports
import constants

# classes
class Course:
    'Course object to hold attributes and functions for a course'

    def __init__(self, id, created, created_by, course_code, name):
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

    @classmethod
    def noID(cls, created, created_by, course_code, name):
        """
        the parameters correspond with the parameters in the constructor above

        returns a new course with the id parameter set as None and the other
        parameters as they are passed in through parameters

        this function acts as a second constructor where you have created a
        course that has not yet been assigned an id from the database
        """
        return cls(None, created, created_by, course_code, name)

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
        self.name        == other.name)

    def setID(self, id):
        """
        self - the course in question
        id   - the id for the course in the database

        this function allows you to assign an id to the course
        'self' after inserting it into the database
        """
        self.id = id

    def __str__(self):
        """
        self - the course in question

        returns a string that fully describes the course 'self'

        this functions allows you to convert the course object
        into a human-readable string for viewing the information
        in it
        """
        string = ""
        string += "id: "          + str(self.id)          + "\n"
        string += "created: "     + str(self.created)     + "\n"
        string += "created by: "  + str(self.created_by)  + "\n"
        string += "course code: " + str(self.course_code) + "\n"
        string += "name: "        +     self.name         + "\n"

        return string
    def toJson(self):
        data = [{
        "id"            : self.id,
        "created"       : self.created,
        "cread_by"      : self.created_by,
        "course_code"   : self.course_code,
        "name"          : self.name
        }]
        return json.dumps(data)

