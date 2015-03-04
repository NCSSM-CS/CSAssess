#!/usr/bin/python3

"""
created_by:         Keshav Patel
created_date:       3/4/2015
last_modified_by:   Keshav Patel
last_modified date: 3/4/2015
"""

# imports
import constants
import json
from sql.user import User
from sql.question import Question
from sql.answer import Answer
from sql.topic import Topic
from sql.session import Session

#Format of answer -KP
#requestType: answer
#course: "string"
#year: "string"
#term: "string"
#period: "string"


def iChooseU(json):
    #from Ebube
    ipAddress = self.client_address[0]
    session = Session.get(json["session"], ipAddress)[0]
    thisUser = User.get(session[0])[0]
    if DEBUG > 1:
        print(thisUser)

    course = json["course"]
    year = json["year"]
    term = json["term"]
    period = json["period"]

    newCourse = Course.noID(TIME_STAMP, thisUser.id, course, year, term, period, ACTIVE)
    newCourse.add()

    successJson = json.dumps({"success":True, "session":session.toJson()})
    return successJson 
