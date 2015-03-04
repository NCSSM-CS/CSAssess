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
from sql.section import Section
from sql.course import Course
from sql.session import Session

#Format of answer -KP
#requestType: answer
#section: "string"
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

    section = json["section"]
    year = json["year"]
    term = json["term"]
    period = json["period"]

    newSection = Section.noID(TIME_STAMP, thisUser.id, course, year, term, period, ACTIVE)
    newSection.add()

    successJson = json.dumps({"success":True, "session":session.toJson()})
    return successJson 
