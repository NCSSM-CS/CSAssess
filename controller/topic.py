#!/usr/bin/python

"""
created_by:         Micah Halter
created_date:       2/28/2015
last_modified_by:   Micah Halter
last_modified date: 3/1/2015
"""

# imports
import constants

# classes
class Topic:
    'Assessment object to hold attributes and functions for an assessment'

    def __init__(self, id, created, created_by, name):
        """
        self       - the topic in question
        id         - the id number of the topic 'self' in the database
        created    - the date when the topic 'self' was created
        created_by - the user that created the topic 'self'
        name       - the name of the topic 'self'

        this function acts as the constructor to define a new topic object
        """
        self.id         = id
        self.created    = created
        self.created_by = created_by
        self.name       = name

    @classmethod
    def noID(cls, created, created_by, name):
        """
        the parameters correspond with the parameters in the constructor above

        returns a new assessment with the id parameter set as None and the other
        parameters as they are passed in

        this function acts as a second constructor where you have created a
        topic that has not yet been assigned an id from the database
        """
        return cls(None, created, created_by, name)

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
        self.name       == other.name)

    def setID(self, id):
        """
        self - the topic in question
        id   - the id for the topc from the database

        this function allows you to assign an id to the topic
        after inserting it into the database
        """
        self.id = id

    def __str__(self):
        """
        self - the topic in question

        returns a string that fully describes the assessment 'self'

        this function allows you to convert the topic object into
        a human-readable string for viewing the information in it
        """
        string = ""
        string += "id: "         + str(self.id)         + "\n"
        string += "created: "    + str(self.created)    + "\n"
        string += "created by: " + str(self.created_by) + "\n"
        string += "name: "       +     self.name        + "\n"
        return string
    def toJson(self):
        data = [{
        "id"        : self.id,
        "created"   : self.created,
        "created by": self.created_by,
        "name"      : self.name
        }]
        return json.dumps(data)

