#!/usr/bin/python3

"""
created_by:         Keshav Patel
created_date:       3/2/2015
last_modified_by:   Keshav Patel
last_modified date: 3/2/2015
"""
"""
TODO: search for test_cases given a question_id
"""

# imports
import constants
import viewUser
import sys

from test_case import Test_Case

import mysql.connector
from mysql_connect_config import getConfig

# functions
def all():
    """
    returns a list of all of the test_case stored on the database

    this function allows for viewing of every test_case in the database
    """

    cnx = mysql.connector.connect(**getConfig("csassess"))
    cursor = cnx.cursor()

    # gets all of the test_case ids stored on the database
    test_caseView = (
            "SELECT t.id "
            "FROM test_case as t;")
    cursor.execute(test_caseView)

    # for every topic id, it created a topic object and
    # adds it to a list to return
    test_case_list = list()
    for (tid) in cursor:
        test_case_list.append(byID(tid))

    cnx.commit()
    cursor.close()
    cnx.close()

    return test_case_list
def byID(test_caseId):
    """
    test_caseId = the id number of the test_case that is wanting to be viewed

    returns a test_case object that has the id for the test_caseId in the database

    this function allows for viewing of a test_case in the database
    """


    cnx = mysql.connector.connect(**getConfig("csassess"))
    cursor = cnx.cursor()

    #gets all of the metadata of the topic at the id 'test_caseId'
    test_caseView = (
            "SELECT t.* "
            "FROM test_case AS t "
            "WHERE t.id=%s" % test_caseId)
    cursor.execute(test_caseView)

    # assigns the needed values to create a new topic object
    # and grabs them from the database
    id = ""
    created = ""
    created_by = ""
    question_id = ""
    weight = ""
    content = ""

    for (tid, tcreated, tcreatedBy, tquestion_id, tweight, tcontent) in cursor:
        id = tid
        created = tcreated
        created_by = tcreatedBy
        question_id = tquestion_id
        weight = tweight
        content = tcontent

    cnx.commit()
    cursor.close()
    cnx.close()

    # calls viewUser to get the needed user object by the id that is
    # held in the metadata of the course
    return Test_Case(id, created, viewUser.byID(created_by), question_id, weight, content)
