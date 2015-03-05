#!/usr/bin/python3

"""
created_by:         Keshav Patel
created_date:       3/4/2015
last_modified_by:   Ebube Chuba
last_modified date: 3/5/2015
"""

# imports
import constants
import json
from sql.user import User
from sql.question import Question
from sql.answer import Answer
from sql.topic import Topic
from sql.session import Session

# Format of course -EC
# requestType: addCourse
# courseCode: "BS402"
# name: "string"


def iChooseU(json):
    thisUser = findUser()

    courseCode = json["courseCode"]
    name = json["name"]

    newCourse = Course.noID(None, thisUser, courseCode, name, ACTIVE)
    newCourse.add()

    return successJson()
