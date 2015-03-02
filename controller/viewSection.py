#!/usr/bin/python

"""
created_by:         Micah Halter
created_date:       3/1/2015
last_modified_by:   Micah Halter
last_modified date: 3/1/2015
"""

# imports
import constants
import viewCourse
import viewUser
import sys

sys.path.insert(0, constants.DIR + "objects")
from section import Section

sys.path.insert(0, constants.DIR)
import mysql.connector
from mysql_connect_config import getConfig

# functions
def byCourse(courseId):
    """
    courseId - the id number of the course that the sections must be linked to

    returns a list of sections that a in the given course id

    this function allows for viewing of every section in a course
    """
    cnx = mysql.connector.connect(**getConfig("csassess"))
    cursor = cnx.cursor()

    # gets all of the section ids linked to the given courseId
    sectionView = (
            "SELECT s.id "
            "FROM section as s "
            "WHERE s.course_id=%s;" % courseId)
    cursor.execute(sectionView)

    # for every section id, it created a section object and
    # adds it to a list to return
    section_list = list()
    for (sid) in cursor:
        section_list.append(byID(sid))

    cnx.commit()
    cursor.close()
    cnx.close()

    return section_list

def byID(sectionId):
    """
    sectionId - the id number of the section that is wanting to be viewed

    returns a section object that has the id of the sectionId in the database

    this function allows for viewing of a section in the database
    """

    cnx = mysql.connector.connect(**getConfig("csassess"))
    cursor = cnx.cursor()

    # gets all of the metadata of the secion at the id 'sectionId'
    sectionView = (
            "SELECT s.* "
            "FROM section AS s "
            "WHERE s.id=%s" % sectionId)
    cursor.execute(sectionView)

    # assigns the needed values to create a new section object
    # and grabs them from the database
    id = ""
    created = ""
    created_by = ""
    course_id = ""
    year = ""
    term = ""
    period = ""

    for (sid, screated, screatedBy, scourseId, syear, sterm, speriod) in cursor:
        id = sid
        created = screated
        created_by = screatedBy
        course_id = scourseId
        year = syear
        term = sterm
        period = speriod

    cnx.commit()
    cursor.close()
    cnx.close()

    # calls viewUser and viewCourse to get the needed objects by the id that is
    # held in the metadata of the section
    return Section(sid, screated, viewUser.byID(screatedBy), viewCourse.byID(scourseId), syear, sterm, speriod)
