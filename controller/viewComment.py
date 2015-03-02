#!/usr/bin/python

"""
created_by:         John Fang
created_date:       3/2/2015
last_modified_by:   John Fang
last_modified date: 3/2/2015
"""

# imports
import constants
import viewUser
import viewAnswer
import sys

from comment import Comment

import mysql.connector
from mysql_connect_config import getConfig

# functions
def all():
    """
    returns a list of all of the comments stored on the database

    this function allows for viewing of every comment in the database
    """

    cnx = mysql.connector.connect(**getConfig("csassess"))
    cursor = cnx.cursor()

    # gets all of the comment ids stored on the database
    commentView = (
            "SELECT c.id "
            "FROM comment as c;")
    cursor.execute(commentView)

    # for every comment id, it created a comment object and
    # adds it to a list to return
    comment_list = list()
    for (cid) in cursor:
        comment_list.append(byID(cid))

    cnx.commit()
    cursor.close()
    cnx.close()

    return comment_list
def byAnswerID(answerId):
    """
    answerId - the id number of the answer that the wanted comments correspond to

    returns a list of all of the comments stored on the database that relate to one answer

    this function allows for viewing of every comment that correspond to an answer in the database
    """

    cnx = mysql.connector.connect(**getConfig("csassess"))
    cursor = cnx.cursor()

    # gets all of the comment ids stored on the database
    commentView = (
            "SELECT c.id "
            "FROM comment as c"
            "WHERE c.answer_id=%s;" % answerId)
    cursor.execute(commentView)

    # for every comment id, it created a comment object and
    # adds it to a list to return
    comment_list = list()
    for (cid) in cursor:
        comment_list.append(byID(cid))

    cnx.commit()
    cursor.close()
    cnx.close()

    return comment_list
def byID(commentId):
    """
    commentId - the id number of the comment that is wanting to be viewed

    returns a comment object that has the id of the commentId in the database

    this function allows for viewing of a comment in the database
    """

    cnx = mysql.connector.connect(**getConfig("csassess"))
    cursor = cnx.cursor()

    #gets all of the metadata of the topic at the id 'topicId'
    commentView = (
            "SELECT c.* "
            "FROM comment AS c "
            "WHERE c.id=%s" % commentId)
    cursor.execute(commentView)

    # assigns the needed values to create a new topic object
    # and grabs them from the database
    id = ""
    created = ""
    created_by = ""
    answer_id = ""
    content = ""

    for (cid, ccreated, ccreatedBy, canswerId, ccontent) in cursor:
        id = cid
        created = ccreated
        created_by = ccreatedBy
        answer_id = canswerId
        content = ccontent

    cnx.commit()
    cursor.close()
    cnx.close()

    # calls viewUser to get the neededuser object by the id that is
    # held in the metadata of the course
    return Comment(id, created, viewUser.byID(created_by), viewAnswer.byID(answer_id), content)
