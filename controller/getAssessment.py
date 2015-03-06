#!/usr/local/bin/python3

"""
created_by:         John Fang
created_date:       3/4/2015
last_modified_by:   Ebube Chuba
last_modified_date: 3/6/2014
"""

# imports
from sql.user import User
from sql.assessment import Assessment
from sql.session import Session
import json

#Format of JSON -KP
#requestType: getAssessment
#name: assessment name      (string)
#user: username             (string)
#section: section name      (string)
#course: course name        (string)
#question: question id      (int)

def iChooseU(form):
    thisUser = utils.findUser(form)

    name = form.getlist("name")[0]
    user = form.getlist("user")[0]
    section = form.getlist("section")[0]
    course = form.getlist("course")[0]
    question = form.getlist("question")[0]

    complete = []
    count = 0

    if not name == "":
        complete += Assessment.get(0, name)
        count += 1
    if not user == "":
        complete += Assessment.get(0, User.get(0, None, user))
        count += 1
    if not section == "":
        complete += Assessment.get(0, Section.get(0, section))
        count += 1
    if not course == "":
        complete += Assessment.get(0, Course.get(0, course))
        count += 1
    if not question == "":
        complete += Assessment.get(0, Question.get(0, question))
        count += 1

    collect = []
    intersect = []

    for response in complete:
        if collect.count(response) < count:
            collect.append(response)
        else:
            intersect.add(response)

    out = {}
    out["assessmentList"] = intersect
    out["sessionID"] = form.getlist("session")[0]

    return json.dumps(out)
