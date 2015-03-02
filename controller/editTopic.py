#!/usr/bin/python

"""
created_by:         Micah Halter
created_date:       2/28/2015
last_modified_by:   Micah Halter
last_modified date: 3/1/2015
"""

"""
TODO:
    - create a newTopic function to generate a new topic object
      add it to the database
"""

# imports
import constants
import sys
import time

from topic import Topic

import mysql.connector
from mysql_connect_config import getConfig


# functions
def newTopic():
    pass
# function to add assessment to database
def addTopic(topic):
    """
    topic - the topic that is being inserted into the database

    this function takes a given topic and inserts it into the database
    """

    cnx = mysql.connector.connect(**getConfig("csassess"))
    cursor = cnx.cursor()

    # writes the topic metadata to the database
    topicWrite = (
            "INSERT INTO topic (created, created_by, name) "
            "VALUES ('%s', %s, '%s');" % (topic.created, topic.created_by.id, topic.name))
    cursor.execute(topicWrite)

    # grabs the id of the newly added topic and sets the object id to it
    topicSelect = (
            "SELECT id FROM topic WHERE created='%s' AND created_by=%s;"
            % (topic.created, topic.created_by.id))
    cursor.execute(topicSelect)

    for (id) in cursor:
        topic.setID(id[-1])

    cnx.commit()
    cursor.close()
    cnx.close()

