#!/usr/bin/python

"""
created_by:         Micah Halter
created_date:       2/28/2015
last_modified_by:   Micah Halter
last_modified date: 3/1/2015
"""

# imports
import constants
import viewTopic
import viewUser
import sys

sys.path.insert(0, "../objects")
from question import Question

sys.path.insert(0, "../")
import mysql.connector
from mysql_connect_config import getConfig

# functions
def all():
    """
    returns a list of all the questions stored on the database

    this function allows for viewing of every course in the database
    """

    cnx = mysql.connector.connect(**getConfig("csassess"))
    cursor = cnx.cursor()

    # gets all of the question ids stored on the database
    questionView = (
            "SELECT q.id "
            "FROM question AS q;")

    cursor.execute(questionView)

    # for every question id, it created a question object and
    # adds it to a list to return
    question_list = list()
    for (id) in cursor:
        question_list.append(byID(id))

    return question_list

def byID(questionId):
    """
    questionId - the id number of the question that is wanting to be viewed

    returns a question object that has the id of the questionId in the database

    this function allows for viewing of a question in the database
    """

    cnx = mysql.connector.connect(**getConfig("csassess"))
    cursor = cnx.cursor()

    # gets all of the metadata of the course at the id 'questionId'
    questionView = (
            "SELECT q.* "
            "FROM question AS q "
            "WHERE q.id=%s" % questionId)

    cursor.execute(questionView)

    # assigns the needed values to create a new question object
    # and grabs them from the database
    id = ""
    created = ""
    created_by = ""
    language = ""
    type = ""
    difficulty = ""
    prev_question_id = ""
    version_number = ""
    last_given = ""
    content = ""

    for (qid, qcreated, qcreatedBy, qlanguage, qtype, qdifficulty, qprevQuestionId, qversionNumber, qlastGiven, qcontent) in cursor:
        id = qid
        created = qcreated
        created_by = qcreatedBy
        language = qlanguage
        type = qtype
        difficulty = qdifficulty
        prev_question_id = qprevQuestionId
        version_number = qversionNumber
        last_give = qlastGiven
        content = qcontent

    # calls topics function to get the needed topic objects by the id
    # that is held in the metadata of the course
    return Question(id, created, viewUser.byID(created_by), language, type, difficulty, prev_question_id, version_number, last_given, content, topics(id))

def topics(questionId):
    """
    questionId - the id number of the question that the topics need to be linked to

    returns a list of topics that are tied to the given 'questionId'

    this function allows a question to get the topics that relate to it
    """

    cnx = mysql.connector.connect(**getConfig("csassess"))
    cursor = cnx.cursor()

    # gets all of the ids of the topics that relate to the given question
    questionTopics = (
        "SELECT t.id "
        "FROM question_topic AS qt "
        "INNER JOIN topic AS t ON qt.topic_id = t.id "
        "INNER JOIN question AS q ON qt.question_id = q.id "
        "WHERE q.id = %s;" % (questionId))

    cursor.execute(questionTopics)

    # adds a new topic object to the return list using the viewTopic
    # module by the ids grabbed from the database
    topic_list = list()
    for (tid) in cursor:
        topic_list.append(viewTopic.byID(tid))

    cnx.commit()
    cursor.close()
    cnx.close()

    # if the debug constant isn't 0, it prints each topic
    if (constants.DEBUG):
        for i in topic_list:
            print(i.toString())

    return topic_list
