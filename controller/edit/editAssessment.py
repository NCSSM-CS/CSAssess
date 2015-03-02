#!/usr/bin/python

"""
created_by:         Micah Halter
created_date:       2/28/2015
last_modified_by:   Micah Halter
last_modified date: 3/1/2015
"""

"""
TODO:
    - figure out how we want to finish up the
      newAssessment generator function
"""

# imports
import sys
import time
import random

sys.path.insert(0, "../objects")
from assessment import Assessment

sys.path.insert(0, "../")
import mysql.connector
from mysql_connect_config import getConfig

# functions
def newAssessment(questionNumber, topic_list):
    """
    questionNumber - number of questions wanted in the new assessment
    topic_list     - list of topics that questions must have to be in assessment

    return

    this function takes a number of questions and a list of topics
    and generates an assignment of the specified length and that
    relates to the given topics
    """

    cnx = mysql.connector.connect(**getConfig("csassess"))
    cursor = cnx.cursor()

    questionSelect =  "SELECT q.id FROM question_topic AS qt "
    questionSelect += "INNER JOIN question AS q ON qt.question_id = q.id "
    questionSelect += "INNER JOIN topic as t ON qt.topic_id = t.id "
    questionSelect += "WHERE"
    for i in range(len(topic_list)):
        questionSelect += (" t.id = %s" % topic_list[i].id)
        if (i != len(topic_list) - 1):
            questionSelect += " OR"
    questionSelect += ";"
    cursor.execute(questionSelect)

    question_list = list()

    # build list of questions that fit the given topics
    for (qid) in cursor:
        question_list.append(viewQuestion.byID(qid))

    assessment_questions = list()
    print(question_list)

    # randomly choose questions from the question_list and add them to the final
    # assessment list and make sure that there are no duplicates
    while (len(assessment_questions) < questionNumber and len(question_list) > 0):
        randomPos = random.randint(0, len(question_list) - 1)
        if (question_list[randomPos] not in assessment_questions):
            assessment_questions.append(question_list[randomPos])
            question_list.pop(randomPos)

    pass
# function to add assessment to database
def addAssessment(assessment):
    """
    assessment - the assessment that is being inserted into the database

    this function takes a given assessment and inserts it into the database
    """

    cnx = mysql.connector.connect(**getConfig("csassess"))
    cursor = cnx.cursor()

    # writes the assessment metadata to the database
    assessWrite = (
            "INSERT INTO assessment (created, created_by, type, section_id, name) "
            "VALUES ('%s', %s, '%s', %s, '%s');" % (assessment.created, assessment.created_by.id, assessment.type, assessment.section.id, assessment.name))
    cursor.execute(assessWrite)

    # grabs the id of the newly added assessment and sets the object id to it
    assessSelect = (
            "SELECT id FROM assessment WHERE created='%s' AND created_by=%s;"
            % (assessment.created, assessment.created_by.id))
    cursor.execute(assessSelect)

    for (id) in cursor:
        assessment.setID(id[0])

    # writes the assessment questions to the assessment_question relationship table
    for i in assessment.question_list:
        assessQuestionWrite = (
            "INSERT INTO assessment_question (assessment_id, question_id) "
            "VALUES (%s, %s);" % (assessment.id, i.id))
        print(assessQuestionWrite)
        cursor.execute(assessQuestionWrite)

    # writes the assessment topics to the assessment_topic relationship table
    for i in assessment.topic_list:
        assessTopicWrite = (
            "INSERT INTO assessment_topic (assessment_id, topic_id) "
            "VALUES (%s, %s);" % (assessment.id, i.id))
        cursor.execute(assessTopicWrite)

    cnx.commit()
    cursor.close()
    cnx.close()

