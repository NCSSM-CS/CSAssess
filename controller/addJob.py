#!/usr/local/bin/python3

"""
created_by: Aninda Manocha
created_date: 3/5/2015
last_modified_by: Aninda Manocha
last_modified_date: 3/5/2015
"""

#imports
import constants
import utils
import json
from sql.session import Session
from sql.user import User
from sql.section import Section
from sql.assessment import Assessment
from sql.job import Job

#Format of job -AM
#section: Section
#jtype: "string"
#assessment: Assessment
#assignedTo: User
#content: "string"
#takenByUser: integer

def iChooseU(json):
    thisUser = utils.findUser(json)

    section = json["section"]
    theSection = Section.get(section["id"])[0]
    jtype = json["jtype"]
    assessment = json["assessment"]
    theAssessment = Assessment.get(assessment["id"])[0]
    assignedTo = json["assignedTo"]
    theAssignedTo = User.get(assignedTo["id"])[0]
    content = json["content"]
    takenByUser = json["takenByUser"]

    newJob = Job.noID(None, thisUser, theSection, jtype, theAssessment, theAssignedTo, content, takenByUser, ACTIVE)
    newJob.add()

    return utils.successJson(json)
