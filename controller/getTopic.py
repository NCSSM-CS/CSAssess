#!/usr/bin/python3

"""
created_by:         Keshav Patel
created_date:       3/4/2015
last_modified_by:   Keshav Patel
last_modified date: 3/4/2015
"""

# imports
from sql.user import User
from sql.topic import Topic
from sql.session import Session

#Format of JSON -KP
#requestType: getAnswer
#name: "string"

def iChooseU(json):
    #from Ebube pt. 2
    ipAddress = self.client_address[0]
    session = Session.get(json["session"], ipAddress)[0]
    thisUser = User.get(session[0])[0]
    if DEBUG > 1:
        print(thisUser)

    name = json["name"]

    aByName = []

    if not name == None:
        aByName.append(Topic.get(0, name))

    out = {}
    
    for num in range(len(aByName)):
        out[num] = aByName[num]

    return json.dumps(out)
