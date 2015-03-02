#!/usr/bin/python

"""
created_by:         Ebube Chuba
created_date:       3/22015
last_modified_by:   Ebube Chuba
last_modified date: 3/2/2015
"""

# imports
import constants
import viewUser
import viewQuestion
import sys

sys.path.insert(0, constants.DIR + "objects")
from answer import Answer
from user import User
from question import Question

sys.path.insert(0, constants.DIR)
import mysql.connector
from mysql_connect_config import getConfig

# functions
def all():
    """
    returns a list of all of the answers stored on the database

    this function allows for viewing of every answer in the database
    """

    cnx = mysql.connector.connect(**getConfig("csassess"))
    cursor = cnx.cursor()

    # gets all of the topic ids stored on the database
    answerView = (
            "SELECT a.id "
            "FROM answer as a;")
    cursor.execute(answerView)

    # for every topic id, it created a topic object and
    # adds it to a list to return
    answer_list = list()
    for (aid) in cursor:
        answer_list.append(byID(aid))

    cnx.commit()
    cursor.close()
    cnx.close()

    return answer_list
def byID(answerId):
    """
    answerId = the id number of the answer that is wanting to be viewed

    returns an answer object that has the id of the ansewrId in the database

    this function allows for viewing of a answer in the database
    """

    cnx = mysql.connector.connect(**getConfig("csassess"))
    cursor = cnx.cursor()

    #gets all of the metadata of the topic at the id 'topicId'
    answerView = (
            "SELECT a.* "
            "FROM answer AS a "
            "WHERE a.id=%s" % answerId)
    cursor.execute(answerView)

    # assigns the needed values to create a new answer object
    # and grabs them from the database
    id = ""
    created = ""
    created_by = ""
    question_id = ""
    score = ""
    answer_text = ""

    for (tid, tcreated, tcreatedBy, tquestionId, tscore, tanswerText) in cursor:
        id = tid
        created = tcreated
        created_by = tcreatedBy
        question_id = tquestionId
        score = tscore
        answer_text = tanswerText

    cnx.commit()
    cursor.close()
    cnx.close()

    # calls viewUser and viewQuestion to get the needed user and question object by the id that is
    # held in the metadata of the answer
    return Answer(id, created, viewUser.byID(created_by), viewQuestion.byId(question_id), score, answer_text)
