#!/usr/bin/python3

"""
created_by:         John Fang
created_date:       3/4/2015
last_modified_by:   Aninda Manocha
last_modified_date: 3/5/2015
"""

# imports
import constants
import utils
import json
from sql.topic import Topic
from sql.session import Session

#Format of topic
#name: "string" 

def iChooseU(json):
    thisUser = findUser()

    name = json["name"]

    newTopic = Topic.noID(None, thisUser, name, ACTIVE)
    newTopic.add()

    return successJson()
