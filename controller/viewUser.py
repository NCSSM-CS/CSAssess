#!/usr/bin/python

'''
created_by:         Micah Halter
created_date:       3/1/2015
last_modified_by:   Micah Halter
last_modified date: 3/1/2015
'''

# imports
import constants
import sys

from user import User

# functions
def all():
    """
    returns a list of all of the users stored on the database

    this function allows for viewing of every user in the database
    """

    return User.get()

def byID(userId):
    """
    userId - the id number of the course that is wanting to be viewed

    returns a user object that has the id of the userId in the database

    this function allows for viewing of a user in the database
    """

    return User.get(userId)
