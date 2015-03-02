#!/usr/bin/env python2.6
"""
created_by:         Samuel Murray
created_date:       3/2/2015
last_modified_by:   Samuel Murray
last_modified date: 3/2/2015
"""

#imports
import sys
import viewTopic
import viewSection
import viewUser
import constants
import viewAssessment

from job import Job

import mysql.connector
from mysql_connect_config import getConfig


#functions
def byAssignedToId(assignedToId):
        """
        assignedToId - the id number of the user that a job is assigned to

        returns an job object that has been assigned to 'assignedToId'

        this function alllows for viewing of a job in the database
        """

        cnx = mysql.connector.connect(**getConfig("csassess"))
        cursor = cnx.cursor()

        # gets all of the metadata of the job at the id 'jobId'
        jobView = (
                "SELECT a.id "
                "FROM job AS a "
                "WHERE a.assigned_to_id=%s;" % assignedToId)
        cursor.execute(jobView)
        # for every assessment id, it creates an assessment object
        # and adds it to a list to return
        job_list = list()
        for (id) in cursor:
            job_list.append(byID(id))

        return job_list
def bySectionID(sectionId):
    """
    sectionId - the id number of the section that assessments pulled must match

    returns a list of jobs that are tied to the given 'sectionId'

    this fucntion allows for viewing of all jobs given to a class
    """

    cnx = mysql.connector.connect(**getConfig("csassess"))
    cursor = cnx.cursor()

    # get all of the job ids that have a given section id
    jobView = (
            "SELECT a.id "
            "FROM job AS a"
            "WHERE a.section_id=%s" % sectionId)
    cursor.execute(jobView)

    # for every assessment id, it creates an assessment object
    # and adds it to a list to return
    job_list = list()
    for (id) in cursor:
        job_list.append(byID(id))

    return job_list
def byID(jobId):
    """
    jobId - the id number of the job that is wanting to be viewed

    returns an job object that has the id of jobId in the database

    this function alllows for viewing of a course in the database
    """

    cnx = mysql.connector.connect(**getConfig("csassess"))
    cursor = cnx.cursor()

    # gets all of the metadata of the job at the id 'jobId'
    jobView = (
            "SELECT a.* "
            "FROM job AS a "
            "WHERE a.id=%s;" % jobId)
    cursor.execute(jobView)

    # assigns the needed values to create a new job object
    # and grabs them from the database
    id = ""
    created = ""
    created_by = ""
    section_id = ""
    type = ""
    assignment_id = ""
    assigned_to_id = ""
    content = ""
    taken_by_user = ""

    for (aid, acreated, acreatedBy, asectionId, atype, aassessmentId, aassignedtoId, acontent, atakenbyuserId) in cursor:
        id = aid
        created = acreated
        created_by = acreatedBy
        section_id = asectionId
        type = atype
        assessment_id = aassessmentId
        assigned_to_id = aassessmentId
        content = acontent
        taken_by_user_id = atakenbyuserId

    # print the values out if the debug constant is not 0
    if (constants.DEBUG):
        print(str(id), created, viewUser.byID(created_by), viewSection.byID(section_id), type,
        viewAssessment.byID(assessment_id), viewUser.byID(assigned_to_id), content, viewUser.byID(taekn_by_user_id))

    cnx.commit()
    cursor.close()
    cnx.close()

    # calls viewUser and viewSection to get the needed objects by the id
    # that is held in the metadata of the job
    # the relationship tables in the database
    return Job(id, created, viewUser.byID(created_by), viewSection.byID(section_id), type, viewAssessment.byID(assessment_id),
    viewUser.byID(assigned_to_id), content, viewUser.byID(taken_by_user_id))
