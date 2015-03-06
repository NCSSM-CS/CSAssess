#!/usr/local/bin/python3

"""
created_by: Aninda Manocha
created_date: 3/5/2015
last_modified_by: Aninda Manocha
last_modified_date: 3/6/2015
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
#section: "string"
#jtype: "string"
#assessment: "string"
#assignedTo: "string"
#content: "string"
#takenByUser: integer

def iChooseU(form):
    thisUser = utils.findUser(form)

    section = Section.get(0, form["section"])[0]
    jtype = json["jtype"]
    assessment = Assessment.get(0, form["assessment"])[0]
    assignedTo = User.get(0, form["assignedTo"])[0]
    content = form["content"]
    takenByUser = form["takenByUser"]

    newJob = Job.noID(None, thisUser, section, jtype, assessment, assignedTo, content, takenByUser, ACTIVE)
    newJob.add()

    return utils.successJson(form)
