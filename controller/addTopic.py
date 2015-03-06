#!/usr/local/bin/python3

"""
created_by:         John Fang
created_date:       3/4/2015
last_modified_by:   Keshav Patel
last_modified_date: 3/6/2015
"""

# imports
import constants
import utils
import json
from sql.user import User
from sql.topic import Topic
from sql.session import Session

#Format of topic
#requestType: addTopic
#name: "string" 

def iChooseU(form):
    thisUser = utils.findUser(form)

    name = form["name"]

    newTopic = Topic.noID(None, thisUser, name, ACTIVE)
    newTopic.add()

    return utils.successJson(form)
