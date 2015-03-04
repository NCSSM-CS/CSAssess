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
#created: TIME_STAMP
#created_by: int
#name: "string"
#active: boolean 

def iChooseU(json):
    ipAddress = self.client_address[0]
    session = Session.get(json["session"], ipAddress)[0]
    thisUser = User.get(session[0])[0]
    if DEBUG > 1:
        print(thisUser)

    name = json("name")

    newTopic = Topic.noID(TIME_STAMP, thisUser.id, name, ACTIVE)
    newTopic.add()

    successJson = json.dumps({"success":True, "session":session.toJson()})
    return successJson
