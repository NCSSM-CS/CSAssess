#!/usr/bin/python

"""
created_by:         John Fang
created_date:       3/2/2015
last_modified_by:   John Fang
last_modified date: 3/2/2015
"""

"""
TODO:
    - create a newComment function to generate a new comment object
      add it to the database
"""

# imports
import constants
import sys
import time

sys.path.insert(0, constants.DIR + "objects")
from comment import Comment

sys.path.insert(0, constants.DIR)
import mysql.connector
from mysql_connect_config import getConfig


# functions
def newComment):
    pass
# function to add comment to database
def addComment(comment):
    """
    comment - the comment that is being inserted into the database

    this function takes a given comment and inserts it into the database
    """

    cnx = mysql.connector.connect(**getConfig("csassess"))
    cursor = cnx.cursor()

    # writes the comment metadata to the database
    commentWrite = (
            "INSERT INTO topic (created, created_by, answer_id, content) "
            "VALUES ('%s', %s, '%s', '%s');" % (comment.created, comment.created_by.id, comment.answer.id, comment.content))
    cursor.execute(commentWrite)

    # grabs the id of the newly added comment and sets the object id to it
    commentSelect = (
            "SELECT id FROM comment WHERE created='%s' AND created_by=%s;"
            % (comment.created, comment.created_by.id))
    cursor.execute(commentSelect)

    for (id) in cursor:
        comment.setID(id[-1])

    cnx.commit()
    cursor.close()
    cnx.close()

