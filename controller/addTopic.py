#!/usr/bin/python3

"""
created_by:         John Fang
created_date:       3/4/2015
last_modified_by:   John Fang
last_modified_date: 3/4/2015
"""

# imports
import constants
import json
from sql.user import User
from sql.topic import Topic
from sql.session import Session

#Format of answer
#name: "string"
#active: boolean 

def iChooseU(json):
    thisUser = findUser()

    name = json("name")

    newTopic = Topic.noID(None, thisUser, name, ACTIVE)
    newTopic.add()

    return successJson()
