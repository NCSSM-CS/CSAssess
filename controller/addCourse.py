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
from sql.question import Question
from sql.answer import Answer
from sql.session import Session
from sql.session import Course

# Format of course -EC
# requestType: addCourse
# courseCode: "string"
# name: "string"


def iChooseU(form):
    thisUser = utils.findUser(form)

    courseCode = form["courseCode"]
    name = form["name"]

    newCourse = Course.noID(None, thisUser, courseCode, name, ACTIVE)
    newCourse.add()

    return utils.successJson(form)
