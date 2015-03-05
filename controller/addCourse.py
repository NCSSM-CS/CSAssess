#!/usr/local/bin/python3

"""
created_by:         Keshav Patel
created_date:       3/4/2015
last_modified_by:   Aninda Manocha
last_modified date: 3/5/2015
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


def iChooseU(json):
    thisUser = utils.findUser(json)

    courseCode = json["courseCode"]
    name = json["name"]

    newCourse = Course.noID(None, thisUser, courseCode, name, ACTIVE)
    newCourse.add()

    return utils.successJson(json)
