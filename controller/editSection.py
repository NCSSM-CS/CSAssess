#!/usr/bin/python

"""
created_by:         Micah Halter
created_date:       2/28/2015
last_modified_by:   Micah Halter
last_modified date: 3/1/2015
"""

"""
TODO:
    - create the newSection function to create a new section object and
      add it to the database
"""

# imports
import constants
import sys
import time

from section import Section

import mysql.connector
from mysql_connect_config import getConfig

# functions
def newSection():
    pass
def addSection(section):
    """
    section - the section that is being inserted into the database

    this function takes a given section and inserts it into the database
    """

    cnx = mysql.connector.connect(**getConfig("csassess"))
    cursor = cnx.cursor()

    # writes the section metadata to the database
    sectionWrite = (
            "INSERT INTO section (created, created_by, course_id, year, term, period) "
            "VALUES ('%s', %s, %s, '%s', '%s', '%s', '%s');" % (section.created, section.created_by.id, section.course_id, section.year, section.term, section.period))
    cursor.execute(sectionWrite)

    # grabs the id of the newly added section and sets the object id to it
    sectionSelect = (
            "SELECT id FROM section WHERE created='%s' AND created_by=%s;"
            % (section.created, section.created_by.id))
    cursor.execute(sectionSelect)

    for (id) in cursor:
        section.setID(id[-1])

    cnx.commit()
    cursor.close()
    cnx.close()

