#!/usr/bin/python3

"""
created_by:         John Fang
created_date:       3/4/2015
last_modified_by:   Keshav Patel
last_modified_date: 3/5/2014
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

def iChooseU(json):
    ipAddress = self.client_address[0]
    session = Session.get(json["session"], ipAddress[0])
    thisUser = User.get(session[0])[0]
    if DEBUG > 1:
        print(thisUser)

    name = json["name"]
    user = json["user"]
    section = json["section"]
    course = json["course"]
    question = json["question"]

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
    out["sessionID"] = json["session"]

    return json.dumps(out)
