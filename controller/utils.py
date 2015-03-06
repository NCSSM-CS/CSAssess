#!/usr/local/bin/python3

# Created by:   Aninda Manocha
# Created date: 3/5/2014
# Last modified by:   Ebube Chuba
# Last modified date: 3/6/2014

import os
from sql.user import User
from sql.session import Session

def findUser(json):
    session = Session.get("1234567890123456789012345678901234567890123456789012345678901234", "127.0.0.1")[0]
    thisUser = session.user
    if DEBUG > 1:
        print(thisUser)
    return thisUser

def successJson(json):
    session = Session.get("1234567890123456789012345678901234567890123456789012345678901234", "127.0.0.1")[0]
    successJson = json.dumps({"success":True, "session":session.toJson()})
    return successJson
