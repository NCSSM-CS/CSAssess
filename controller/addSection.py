#!/usr/local/bin/python3

"""
created_by:         Keshav Patel
created_date:       3/4/2015
last_modified_by:   Keshav Patel
last_modified date: 3/6/2015
"""

# imports
import constants
import json
from sql.user import User
from sql.section import Section
from sql.course import Course
from sql.session import Session

#Format of answer -AM
#requestType: addSection
#course: Course
#year: "string"
#term: "string"
#period: "string"

def iChooseU(form):
    thisUser = utils.findUser(form)

    course = form["course"]
    theCourse = Course.get(course["id"])[0]
    year = form["year"]
    term = form["term"]
    period = form["period"]

    newSection = Section.noID(None, thisUser, theCourse, year, term, period, ACTIVE)
    newSection.add()

    return utils.successJson(form)
