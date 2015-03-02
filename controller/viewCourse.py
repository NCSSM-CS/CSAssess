#!/usr/bin/python

"""
created_by:         Micah Halter
created_date:       3/1/2015
last_modified_by:   Micah Halter
last_modified date: 3/1/2015
"""

# imports
import constants
import viewUser
import sys

from course import Course

import mysql.connector
from mysql_connect_config import getConfig

# functions
def all():
    """
    returns a list of all of the courses stored on the database

    this function allows for viewing of every course in the database
    """

    cnx = mysql.connector.connect(**getConfig("csassess"))
    cursor = cnx.cursor()

    # gets all of the course ids stored on the database
    courseView = (
            "SELECT c.id "
            "FROM course AS c;")
    cursor.execute(sqlCall())

    # for every course id, it created a course object and
    # adds it to a list to return
    course_list = list()
    for (id) in cursor:
        course_list.append(byID(id))

    return question_list

def byID(courseId):
    """
    courseId - the id number of the course that is wanting to be viewed

    returns a course object that has the id of the courseId in the database

    this function allows for viewing of a course in the database
    """

    cnx = mysql.connector.connect(**getConfig("csassess"))
    cursor = cnx.cursor()

    # gets all of the metadata of the course at the id 'courseId'
    courseView = (
            "SELECT c.* "
            "FROM course AS c "
            "WHERE c.id=%s" % courseId)
    cursor.execute(courseView)

    # assigns the needed values to create a new assessment object
    # and grabs them from the database
    id = ""
    created = ""
    created_by = ""
    course_code = ""
    name = ""

    for (cid, ccreated, ccreatedBy, ccourseCode, cname) in cursor:
        id = cid
        created = ccreated
        created_by = ccreatedBy
        course_code = ccourseCode
        name = cname

    cnx.commit()
    cursor.close()
    cnx.close()

    # calls viewUser to get the needed user object by the id that is
    # held in the metadata of the course
    return Course(cid, ccreated, viewUser.byID(ccreatedBy), ccourseCode, cname)
