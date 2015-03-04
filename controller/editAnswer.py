#!/usr/bin/python3

"""
created_by:         Ebube Chuba
created_date:       3/2/2015
last_modified_by:   Ebube Chuba
last_modified date: 3/2/2015
"""

"""
TODO:
    - create a newAnswer function to generate a new answer object
      add it to the database
"""

# imports
import constants
import sys
import time

from answer import Answer

import mysql.connector
from mysql_connect_config import getConfig


# functions
def newAnswer():
    pass
# function to add assessment to database
def addAnswer(answer):
    """
    answer - the answer that is being inserted into the database

    this function takes a given answer and inserts it into the database
    """

    cnx = mysql.connector.connect(**getConfig("csassess"))
    cursor = cnx.cursor()

    # writes the topic metadata to the database
    answerWrite = (
            "INSERT INTO answer (created, created_by, question, score, answer_text) "
            "VALUES ('%s', %s, '%s', '%s', '%s');" % (answer.created, answer.created_by.id, answer.question.id, answer.score, answer.answer_text))
    cursor.execute(answerWrite)

    # grabs the id of the newly added topic and sets the object id to it
    answerSelect = (
            "SELECT id FROM answer WHERE created='%s' AND created_by=%s;"
            % (answer.created, answer.created_by.id))
    cursor.execute(topicSelect)

    for (id) in cursor:
        answer.setID(id[-1])

    cnx.commit()
    cursor.close()
    cnx.close()

