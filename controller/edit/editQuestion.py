#!/usr/bin/python

"""
created_by:         Micah Halter
created_date:       2/28/2015
last_modified_by:   Micah Halter
last_modified date: 3/1/2015
"""

# imports
import constants
import sys
import time

sys.path.insert(0, "../objects")
from question import Question

sys.path.insert(0, constants.DIR)
import mysql.connector
from mysql_connect_config import getConfig

# functions
def newQuestion(created_by, language, type, difficulty, prev_question_id, version_number, content, topic_list):
    """
    created_by       - the user that the question is being created by
    language         - the programming lanuage that the question is written for
    type             - the type of question is being generated
    difficulty       - the difficulty of the question being made
    prev_question_id - the previous version question id
    version_number   - the version number of the question
    content          - the content of the question
    topic_list       - teh list of topics that apply to this question

    this function takes the parameters of a question and adds a new question entry
    into the database
    """
    newQuestion = Question(time.strftime("%Y-%m-%d %H:%M:%S"), created_by, language, type, difficulty, prev_question_id, version_number, content, topic_list)
    addQuestion(newQuestion)
# function to add assessment to database
def addQuestion(question):
    """
    question - the question that is being inserted into the database

    this function takes a given question and inserts it into the database
    """

    cnx = mysql.connector.connect(**getConfig("csassess"))
    cursor = cnx.cursor()

    # writes the question metadata to the database
    questionWrite = (
            "INSERT INTO question (created, created_by, language, type, difficulty, prev_question_id, version_number, last_given, content) "
            "VALUES ('%s', %s, '%s', '%s', '%s', %s, %s, %s, '%s');" % (question.created, question.created_by.id, question.language, question.type, question.difficulty, question.prev_question_id if question.prev_question_id != None else "NULL", question.version_number, "'" + question.last_given + "'" if question.last_given != '' else "NULL", question.content))
    cursor.execute(questionWrite)

    # grabs the id of the newly added question and sets the object id to it
    questionSelect = (
            "SELECT id FROM question WHERE created='%s' AND created_by=%s;"
            % (question.created, question.created_by.id))
    cursor.execute(questionSelect)

    for (id) in cursor:
        question.setID(id[-1])

    # writes the question topics to the question_topic relationship table
    for i in question.topic_list:
        questionTopicWrite = (
            "INSERT INTO question_topic (question_id, topic_id) "
            "VALUES (%s, %s);" % (question.id, i.id))
        cursor.execute(questionTopicWrite)

    cnx.commit()
    cursor.close()
    cnx.close()

