#!/usr/bin/python

"""
created_by:         Micah Halter
created_date:       2/28/2015
last_modified_by:   Micah Halter
last_modified date: 3/1/2015
"""

# imports
import sys
import viewQuestion
import viewTopic
import viewSection
import viewUser
import constants

sys.path.insert(0, "../objects")
from assessment import Assessment

sys.path.insert(0, "../")
import mysql.connector
from mysql_connect_config import getConfig

# functions
def bySectionID(sectionId):
    """
    sectionId - the id number of the section that assessments pulled must match

    returns a list of assessments that are tied to the given 'sectionId'

    this fucntion allows for viewing of all assessments given to a class
    """

    cnx = mysql.connector.connect(**getConfig("csassess"))
    cursor = cnx.cursor()

    # get all of the assessment ids that have a given section id
    assessView = (
            "SELECT a.id "
            "FROM assessment AS a"
            "WHERE a.section_id=%s" % sectionId)
    cursor.execute(assessView)

    # for every assessment id, it creates an assessment object
    # and adds it to a list to return
    assessment_list = list()
    for (id) in cursor:
        assessment_list.append(byID(id))

    return assessment_list

def byID(assessId):
    """
    assessId - the id number of the assessment that is wanting to be viewed

    returns an assessment object that has the id of assessId in the database

    this function alllows for viewing of a course in the database
    """

    cnx = mysql.connector.connect(**getConfig("csassess"))
    cursor = cnx.cursor()

    # gets all of the metadata of the assessment at the id 'assessId'
    assessView = (
            "SELECT a.* "
            "FROM assessment AS a "
            "WHERE a.id=%s;" % assessId)
    cursor.execute(assessView)

    # assigns the needed values to create a new assessment object
    # and grabs them from the database
    id = ""
    created = ""
    created_by = ""
    type = ""
    section_id = ""
    name = ""

    for (aid, acreated, acreatedBy, atype, asectionId, aname) in cursor:
        id = aid
        created = acreated
        created_by = acreatedBy
        type = atype
        section_id = asectionId
        name = aname

    # print the values out if the debug constant is not 0
    if (constants.DEBUG): print(str(id), created, viewUser.byID(created_by), type, viewSection.byID(section_id), name)

    cnx.commit()
    cursor.close()
    cnx.close()

    # calls viewUser and viewSection to get the needed objects by the id
    # that is held in the metadata of the assessment
    # also calls the question and topics functions to get the questions from
    # the relationship tables in the database
    return Assessment(id, created, viewUser.byID(created_by), type, viewSection.byID(section_id), name, questions(id), topics(id))

def questions(assessId):
    """
    assessId - the assessment id used to find the questions associated with it

    returns a list of the questions in the assessment

    this function will take an assessmentId, connect to the assessment_question
    relationship table and return a list of questions
    """

    cnx = mysql.connector.connect(**getConfig("csassess"))
    cursor = cnx.cursor()

    # grab the ids for all of the questions tied to the assessment
    assessQuestions = (
        "SELECT q.id "
        "FROM assessment_question AS aq "
        "INNER JOIN question AS q ON aq.question_id = q.id "
        "INNER JOIN assessment AS a ON aq.assessment_id = a.id "
        "WHERE a.id = %s;" % (assessId))

    cursor.execute(assessQuestions)

    question_list = []

    for (qid) in cursor:
        question_list.append(viewQuestion.byID(qid))

    cnx.commit()
    cursor.close()
    cnx.close()

    # if the debug constant isn't 0, then print each question
    if (constants.DEBUG):
        for i in question_list:
            print(i.toString())

    return question_list

def topics(assessId):
    """
    assessId - the assessment id used to find the topics associated with it

    returns a list of the topics in the assessment

    this function will take an assessmentId, connect to the assessment_topic
    relationship table and return a list of topics
    """

    cnx = mysql.connector.connect(**getConfig("csassess"))
    cursor = cnx.cursor()

    # grab the ids for all of the topics tied to the assessment
    assessTopics = (
        "SELECT t.id "
        "FROM assessment_topic AS at "
        "INNER JOIN topic AS t ON at.topic_id = t.id "
        "INNER JOIN assessment AS a ON at.assessment_id = a.id "
        "WHERE a.id = %s;" % (assessId))

    cursor.execute(assessTopics)

    topic_list = list()

    for (tid) in cursor:
        topic_list.append(viewTopic.byID(tid))

    cnx.commit()
    cursor.close()
    cnx.close()

    # if the debug constant isn't 0, then print each topic
    if (constants.DEBUG):
        for i in topic_list:
            print(i.toString())

    return topic_list
