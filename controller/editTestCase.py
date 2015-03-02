#!/usr/bin/python

"""
created_by:         Keshav Patel
created_date:       3/2/2015
last_modified_by:   Keshav Patel
last_modified date: 3/2/2015
"""

# imports
import constants
import sys
import time

from test_case import Test_Case

import mysql.connector
from mysql_connect_config import getConfig


# functions
def newTest_Case():
    pass
# function to add assessment to database
def addTest_Case(test_case):
    """
    test_case - the test_case that is being inserted into the database

    this function takes a given test_case and inserts it into the database
    """

    cnx = mysql.connector.connect(**getConfig("csassess"))
    cursor = cnx.cursor()

    # writes the topic metadata to the database
    topicWrite = (
            "INSERT INTO test_case (created, created_by, question_id, weight, content) "
            "VALUES ('%s', %s, '%s');" % (test_case.created, test_case.created_by.id, test_case.question_id, test_case.weight, test_case.content))
    cursor.execute(test_caseWrite)

    # grabs the id of the newly added topic and sets the object id to it
    test_caseSelect = (
            "SELECT id FROM test_case WHERE created='%s' AND created_by=%s;"
            % (test_case.created, test_case.created_by.id))
    cursor.execute(test_caseSelect)

    for (id) in cursor:
        test_case.setID(id[-1])

    cnx.commit()
    cursor.close()
    cnx.close()

