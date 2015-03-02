#!/usr/bin/python

"""
created_by:         Micah Halter
created_date:       2/28/2015
last_modified_by:   Micah Halter
last_modified date: 3/1/2015
"""

# imports
import constants
import viewUser
import sys

sys.path.insert(0, "../objects")
from topic import Topic

sys.path.insert(0, "../")
import mysql.connector
from mysql_connect_config import getConfig

# functions
def all():
    """
    returns a list of all of the topics stored on the database

    this function allows for viewing of every topic in the database
    """

    cnx = mysql.connector.connect(**getConfig("csassess"))
    cursor = cnx.cursor()

    # gets all of the topic ids stored on the database
    topicView = (
            "SELECT t.id "
            "FROM topic as t;")
    cursor.execute(topicView)

    # for every topic id, it created a topic object and
    # adds it to a list to return
    topic_list = list()
    for (tid) in cursor:
        topic_list.append(byID(tid))

    cnx.commit()
    cursor.close()
    cnx.close()

    return topic_list
def byID(topicId):
    """
    topicId = the id number of the topic that is wanting to be viewed

    returns a topic object that has the id fo the topicId in the database

    this function allows for viewing of a topic in the database
    """

    cnx = mysql.connector.connect(**getConfig("csassess"))
    cursor = cnx.cursor()

    #gets all of the metadata of the topic at the id 'topicId'
    topicView = (
            "SELECT t.* "
            "FROM topic AS t "
            "WHERE t.id=%s" % topicId)
    cursor.execute(topicView)

    # assigns the needed values to create a new topic object
    # and grabs them from the database
    id = ""
    created = ""
    created_by = ""
    name = ""

    for (tid, tcreated, tcreatedBy, tname) in cursor:
        id = tid
        created = tcreated
        created_by = tcreatedBy
        name = tname

    cnx.commit()
    cursor.close()
    cnx.close()

    # calls viewUser to get the neededuser object by the id that is
    # held in the metadata of the course
    return Topic(id, created, viewUser.byID(created_by), name)
