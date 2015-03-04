#!/usr/bin/env python3
"""
created_by:         Samuel Murray
created_date:       3/2/2015
last_modified_by:   Samuel Murray
last_modified date: 3/2/2015
"""
#imports
import constants
import sys
import time

from job import Job

import mysql.connector
from mysql_connect_config import getConfig

"""
TODO:
    -Make adn addJob function that adds a newly created question to the database.
"""

#functions
def newJob(createdBy, sectionId, type, assessmentID, assignedToID, content, takenByUserID):
    """
    createdBy - the user that created the job
    sectionID - the section that the job falls under
    type - the type of job
    assessmentID - the assessment to which a job refers
    assignedToID - the user to which a job is assigned
    content - the content of a job
    takenByUserID - the user taking a job

    This function takes the parameters and creates a new Job object.
    """
    newJob = Job.noID(time.strftime("%Y-%m-%d %H:%M:%S"), createdBy, sectionID, type,
    assessmentID, assignedToID, content, takenByUserID)
    addJob(newJob)

# function to add Job to database
def addJob(job):
    pass
