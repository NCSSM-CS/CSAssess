#!/usr/bin/python

"""
created_by:         EZ
created_date:       3/2/2015
last_modified_by:   EZ
last_modified date: 3/2/2015
"""

"""
TODO:
    - create the newCourse functio to create a new course object
      and add it to the database
"""

# imports
import sys
import time

sys.path.insert(0, "../objects")
from course import Course

sys.path.insert(0, "../")
import mysql.connector
from mysql_connect_config import getConfig

# functions
def newCourse():
    pass
def addCourse(course):
    """
    course - the course that is being inserted into the database

    this function takes a given course and inserts it into the database
    """

    cnx = mysql.connector.connect(**getConfig("csassess"))
    cursor = cnx.cursor()

    # writes the course metadata to the database
    courseWrite = (
            "INSERT INTO course (created, created_by, course_code, name) "
            "VALUES ('%s', %s, '%s', '%s');" % (course.created, course.created_by.id, course.couse_code, course.name))
    cursor.execute(courseWrite)

    # grabs the id of the newly added course and sets the object id to it
    couseSelect = (
            "SELECT id FROM course WHERE created='%s' AND created_by=%s;"
            % (course.created, course.created_by.id))
    cursor.execute(courseSelect)

    for (id) in cursor:
        course.setID(id[-1])

    cnx.commit()
    cursor.close()
    cnx.close()
