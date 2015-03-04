#!/usr/bin/python3

"""
created_by:         John Fang
created_date:       3/4/2015
last_modified_by:   John Fang
last_modified_date: 3/4/2014
"""

# imports
from sql.user import User
from sql.assessment import Assessment
from sql.session import Session
import json

def iChooseU(json):
    ipAddress = self.client_address[0]
    session = Session.get(json["session"], ipAddress[0])
    thisUser = User.get(session[0])[0]
    if DEBUG > 1:
        print(thisUser)
    
    out = {}
    for num in len(range(Assessment.get(thisUser.id))):
        out[num] = Assessment.get(thisUser.id)[num]
    
    return json.dumps(out)

